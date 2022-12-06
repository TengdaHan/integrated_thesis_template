vgg_bibtex
==========

VGG maintains a BibTeX repository of citations. This helps to maintain continuity between publications, and saves time in looking up references. The VGG Web-based publications system  (see the [VGG internal Wiki](http://www.robots.ox.ac.uk/~vgg/internal/wiki/doku.php/vgg_pub_bibtex)) makes it easy to add your papers to the list of VGG pubications; it also automatically maintains a part of the BibTeX repository.

The BibTeX repository consists of the following files:

* vgg_local.bib - BibTeX file storing publications made by VGG
* vgg_other.bib - BibTeX file storing publications made by other groups, but cited in our papers
* longstrings.bib - BibTeX file storing full names of conferences and journals including the location if possible (e.g. “cvpr08” unfolds into “Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Anchorage, Alaska”)
* shortstrings.bib - BibTeX file storing shortened names of conferences and journals; useful for conference submissions where space may be tight (e.g. “cvpr08” unfolds into “Proc. CVPR”)

**The repository version of `vgg_local.bib` is updated `automatically` by the publications system every time someone adds their paper to the system**. Therefore, any changes done manually will be LOST.

**The only BibTeX file which is supposed to be edited manually by a user is `vgg_other.bib`**. Users wanting to edit this file need to **request permission first to the maintainers** (see the [VGG internal Wiki](http://www.robots.ox.ac.uk/~vgg/internal/wiki/doku.php/vgg_pub_bibtex)), indicating their GitLab user.

If you need to add a conference or journal to `longstrings.bib` and `shortstrings.bib`, **please contact the maintainers** (see the [VGG internal Wiki](http://www.robots.ox.ac.uk/~vgg/internal/wiki/doku.php/vgg_pub_bibtex)).

### Additional script for integrated thesis template
* group_bib.py - A python script to group multiple bibliography source files but still keeps compatiable to original tex files.
