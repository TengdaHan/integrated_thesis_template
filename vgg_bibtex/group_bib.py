import os
import re
import tqdm

p_bib_type = re.compile(r'@([^{]*)')
p_bib_id = re.compile(r'{([^(,|\n)]*)')
p_bib_title = re.compile(r'(?i)(?<![a-z])title(( |\t)*=)([^(,|\n)]*)')

def process_one_bib(text):
    """read one bib item from text, get required values."""
    text = text.strip()
    assert text.startswith('@')
    bib_type = p_bib_type.search(text).group(1)
    bib_id = p_bib_id.search(text).group(1)
    try:
        bib_tag = p_bib_title.search(text).group(0)
        bib_tag = bib_tag[len('title')::].lstrip()[1::].strip()
        bib_tag = bib_tag.replace('{','').replace('}','').lower()
    except:
        assert (bib_type.lower() not in ['inproceedings', 'article'])
        bib_tag = bib_id
    bib_tag += f'_{bib_type.lower()}'
    return {'bib_type': bib_type, 'bib_id': bib_id, 'bib_tag': bib_tag, 'text': text}


def main(filelist):
    """Group multiple bib source files into a single file.
    Remove duplicate items by checking the title, 
    add additional 'IDS' key to support referencing without changing tex files.
    
    E.g.    
    @InProceedings{Someone99a,
    title="paper title",
    IDS={"SomeOne99"},
    ...
    }
    
    -- this item can be cited by either \cite{Someone99a} or \cite{SomeOne99}.

    """

    print(f'processing bib source: {filelist}')
    out_text = ''
    all_bib_dict = {}

    for fpath in filelist:
        with open(fpath) as fobj:
            content = fobj.readlines()
        content = [i for i in content if not i.lstrip().startswith('%')]
        content = ''.join(content)
        
        items = content.split('@')
        items = ['@'+i.strip() for i in items if i.strip() != '']
        for item in tqdm.tqdm(items, total=len(items), disable=True):
            bib_dict = process_one_bib(item)
            tag = bib_dict['bib_tag']

            if tag in all_bib_dict:
                if 'IDS' not in all_bib_dict[tag]:
                    all_bib_dict[tag]['IDS'] = [bib_dict['bib_id']]
                else:
                    all_bib_dict[tag]['IDS'].append(bib_dict['bib_id'])
            else:
                all_bib_dict[tag] = {'dict': bib_dict}

        print(f"bib count: {len(all_bib_dict)}")


    tag_id_list = sorted(
        [(k, v['dict']['bib_id']) for k,v in all_bib_dict.items()], 
        key=lambda x: x[-1])

    for tag,_ in tag_id_list:
        bib_dict = all_bib_dict[tag]
        if 'IDS' not in bib_dict:
            out_text += bib_dict['dict']['text']
        else:
            text = bib_dict['dict']['text']
            ids = bib_dict['IDS']
            ids = [f'"{i}"' for i in ids]
            id_string = f"IDS={{{','.join(ids)}}},"
            id_string = ",\n"+id_string+"\n}"
            if text.endswith('\n}'):
                text = text[0:-2].rstrip()
            elif text.endswith('}'):
                text = text[0:-1].rstrip()
            if text.endswith(','):
                text += id_string[1::]
            else:
                text += id_string
            out_text += text
            
            print(text)
            import ipdb; ipdb.set_trace()
        out_text += '\n\n'


    with open('grouped_bib.bib', 'w') as fobj:
        fobj.write(out_text)


if __name__ == '__main__':
    filelist = ['vgg_local.bib', 'vgg_other.bib', '../chapter/paper1/egbib.bib']
    main(filelist)
