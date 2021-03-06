# II. Taxonomy of Functions
## Précis
*The premise of this section is to classify and explicate the functions within this portfolio by looking at the functions through the prism of taxonomy. This section aims to create a logical and intuitive trinomial nomenclature framework, modeled after the binomial nomenclature classification of systematics, for naming and abbreviating of functions within this portfolio, enabling functions such as* `experiment_with_XGB` *to be shortened to* `ewXG` *and* `comparison_plot_surface_XGB` *to* `cpXG`*. None of these abbreviations were used in future sections in case the reader had not familiarized themselves with this section, but all abbreviations are performant and ergo can be used in the coding playground. So to illustrate the implementation of this section, the subsection* `A. Demo` *found in the* `README.md` *at this repository's homepage was recoded with abbreviated functions in subsection* `G. Exhibition`*.*


## Author's Note
*The method of documentation presented in this section is more a creative flourish than an essential read. Conventional documentation can be found on any method below with the* `help` *command or in the function's code as docstring and commented code.* 

*Please note in biological taxonomic classifications, only the genus (first letter capitalized) and species (not capitalized) is italicized to identify an organism in a system called binomial nomenclature. Here, trinomial nomenclature with adapted classifications, format typography, and abbreviations will be used to classify and explicate functions and attendant "ecosystems."* 

*Function "ecosystems" represented a group of functions that worked in a synergistic fashion and each section within this portfolio after this section was designated its own "ecosystem." While a whimsical liberty was taken in the naming of "ecosystems," some more apropos than others, these names should not be impediment to comprehension and do not serve any special purpose beyond continuing the environmental-taxonomical biologist lens of expounding. This is not an exhaustive list of all functions but rather a strategic collection of functions that may be most confusing at first glance and/or with synergistic functionality.*


## Table of Contents
*To ever return to the Table of Contents click the  :point_up_2:  located to the far right of the subsection title.*
### II. Taxonomy of Functions <!-- &emsp was used to demarcate indents--> 
#### &emsp;&emsp; [A. Adaptations](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#a-adaptations---point_up_2)

&emsp;&emsp;&emsp;&emsp; [i. Classifications](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#i-classifications)

&emsp;&emsp;&emsp;&emsp; [ii. Format Typography](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#ii-format-typography)

&emsp;&emsp;&emsp;&emsp; [iii. Abbreviation](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#iii-abbreviations)

#### &emsp;&emsp; [B. Family](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#b-family---point_up_2)

&emsp;&emsp;&emsp;&emsp; [`experiment`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#experiment)

&emsp;&emsp;&emsp;&emsp; [`for_`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#for_)

&emsp;&emsp;&emsp;&emsp; [`plot`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#plot)

&emsp;&emsp;&emsp;&emsp; [`interactive`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#interactive)

&emsp;&emsp;&emsp;&emsp; [`comparison`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#comparison)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [Prefixes](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#prefixes)

&emsp;&emsp;&emsp;&emsp; [`optimize`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#optimize)

&emsp;&emsp;&emsp;&emsp; [`intialize`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#initialize)

&emsp;&emsp;&emsp;&emsp; [`zoom`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#zoom)


#### &emsp;&emsp; [C. Genus](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#c-genus---point_up_2)

&emsp;&emsp;&emsp;&emsp; [Family of `experiment`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#family-of-experiment)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_with`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_with)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`4D_with`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#4D_with)

&emsp;&emsp;&emsp;&emsp; [Family of `for_`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#family-of-for_)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_3D_plot`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_3D_plot)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_3D_comp`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_3D_comp)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`4D_plot`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#4D_plot)

&emsp;&emsp;&emsp;&emsp; [Family of `plot`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#family-of-plot)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_wireframe`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_wireframe)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_surface`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_surface)

&emsp;&emsp;&emsp;&emsp; [Family of `interactive`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#family-of-interactive)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_surface`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_surface-1)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_4Dsurface`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_4Dsurface)

&emsp;&emsp;&emsp;&emsp; [Family of `comparison`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#family-of-comparison)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_Grid_Search`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_Grid_Search)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_plot_surface`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_plot_surface)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_interactive_surface`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_interactive_surface)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_to_table`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_to_table)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_plot`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_plot)

&emsp;&emsp;&emsp;&emsp; [Family of `zoom`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#family-of-experiment)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_3D`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_3D)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_4D`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_4D)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [Without `zoom` vs. With `zoom`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#without-zoom-vs-with-zoom)

#### &emsp;&emsp; [D. Species](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#d-species---point_up_2)
&emsp;&emsp;&emsp;&emsp; [Ecosystemic](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#ecosystemic)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_DT`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_DT)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_Forest`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_Forest)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_XGB`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_XGB)

&emsp;&emsp;&emsp;&emsp; [Niche](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#niche)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_plot`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_plot-1)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_Pipeline`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_Pipeline)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [`_pipelineCV_Forest`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#_pipelineCV_Forest)

#### &emsp;&emsp; [E. Tabular Presentation](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#e-tabular-presentation---point_up_2)
&emsp;&emsp;&emsp;&emsp; [Table 1. Function Assembly](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-1-function-assembly)

&emsp;&emsp;&emsp;&emsp; [Table 2. Function Abbreviation](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-2-function-abbreviation)

&emsp;&emsp;&emsp;&emsp; [Table 3. Function Purpose](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-3-function-purpose)

&emsp;&emsp;&emsp;&emsp; [Table 4. Interactive Master List](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-4-interactive-master-list)


#### &emsp;&emsp; [F. Ecosystems](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#f-ecosystems---point_up_2)
&emsp;&emsp;&emsp;&emsp; [i. Keystone Species](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#i-keystone-species)

&emsp;&emsp;&emsp;&emsp; [ii. Decision Tree (Section III)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#ii-decision-tree-section-iii)

&emsp;&emsp;&emsp;&emsp; [iii. Random Forest (Section IV)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#iii-random-forest-section-iv)

&emsp;&emsp;&emsp;&emsp; [iv. Random Rainforest - Imputation & Encoding for Forest (Section V)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#iv-random-rainforest---imputation--encoding-for-forest-section-v)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [a. Soil Percolation - Imputation (Section V.A)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#a-soil-percolation---imputation-section-va)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [b. Canopy Percolation - Encoding (Section V.B)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#b-canopy-percolation---encoding-section-vb)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [c. Rain & Weather - Pipeline & K-Fold CV (Section V.C)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#c-rain--weather---pipeline--k-fold-cv-section-vc)

&emsp;&emsp;&emsp;&emsp; [v. Mountain - XGB Regressor (Section VI)](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#v-mountain---xgb-regressor-section-vi)

#### &emsp;&emsp; [G. Exhibition](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#g-exhibition---point_up_2)

&emsp;&emsp;&emsp;&emsp; [Excerpts & Annotations](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#excerpts--annotations)

&emsp;&emsp;&emsp;&emsp; [Demo 2.0](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#demo-20)

#### &emsp;&emsp; [H. Areas of Improvement](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#h-areas-of-improvement---point_up_2)

&emsp;&emsp;&emsp;&emsp; [Trinomial Nomenclature System](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#trinomial-nomenclature-system)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [Counterclaim](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#counterclaim)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [Ambiguity](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#ambiguity)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [Functional vs. Argumentative](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#functional-vs-argumentative)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; [Simplicity](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#simplicity)

&emsp;&emsp;&emsp;&emsp; [Holistic Section](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#holistic-section)

## A. Adaptations <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)

### i. Classifications
* `Family Genus Species`
  * Some families have *prefixes* in addition to the root name
    * For instance, within the family `comparison`, there are the three prefixes `time_`, `opt_`, and `multi`, which can be concatenated
* Trinomial Nomenclature
<hr width="3%">

### ii. Format Typography
* Will not be italicized
* Will be formatted as code like this: `code`
* Capitalization will be determined by the individual names rather than collective ranks
<hr width="3%">

### iii. Abbreviations
* Will not follow *Genus species* becomes *G. species*
* Instead, `Family Genus Species` becomes `F.G.Species`
* **Important Truncation Rules:**
  * Capitalization will follow rule declared in ii. Format Typography
    * i.e. `Family genus SPECIES` becomes `F.g.SPECIES`
  * Underscores and special characters will be ignored in abbreviation
    * i.e. only the first letter will be used in abbreviation
  * First letter of the prefix will be appended with a hyphen to the conventional abbreviation
    * i.e. multicomparison_plot_surface_Forest with prefix `multi` abbreviates to `m-c.p.Fo`
  * If there is no `Genus`, abbreviation, standard abbreviation rules still apply
    * i.e. `Family Species` becomes `F.Sp` like the function `initialize_DT` which abbreviates to `i.DT`
    * Though irksomely illogical in context of biology taxonomical paradigm which inspired its conception, the rule enables the classification of more functions
  * **Conflict Clause**: In the event that the same abbreviation will be used for two or more distinct functions, then the `Genus` will be appended to these abbreviations one letter at a time until no two functions have the same abbreviation.
    * i.e. `for_3D_plot_Forest` and `for_3D_comp_Forest` respectively become `f.3Dp.Fo` and `f.3Dc.Fo`
  * **Hypothetical Extension of Conflict Clause**: Although no instance occurs where the aforementioned conflict clause enumerating the `Genus` letter by letter does not fail to distinguish multiple function's abbreviations, if such example were to occur theoretically, then the `Family`, `Species`, and `Prefix` in that order would be enumerated in the same fashion until the same aim of unique abbreviations for each function is accomplished. This rule would most likely be called upon in circumstances where there is the function has no `Genus` and would ergo seldom apply.
* **Coding Implementation:**
  * Equivalent functions will be available in both the abbreviated and unabbreviated in the coding environment, but only the unabbreviated versions will be used in section in case the reader has not familiarized themselves with this section.
  * The abbreviated function name retains all the capitalization but the period mark demarcating classification rank will be removed
    * i.e. The abbreviation `f.3Dp.Fo` (returns 3D plottable dictionary data) or `e.w.XG` (bivariate hyperparamter optimization of XGBR) become respectively `f3DpFo(...)` and `ewXG(...)` and are equivalent to the corresponding functions `for_3D_comp_Forest` and `experiment_with_XGB`
  * Prefixes separated by the hyphen `-` in standard abbreviation formatting will become an underscore as `_` for coding implementation
    * i.e. The abbreviation `m-c.p.Fo` (plots multiple 3D surface plots) becomes `m_cpFo`which is equivalent to `multicomparison_plot_surface_Forest`
  * Since no abbreviated functions were used in future sections, a exhibition of this section's contributions can be found in the uninventively-titled subsection [`G. Exhibition`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#g-exhibition---point_up_2)
    * The subsection abbreviates the functions used in the subsection `A. Demo` in section `I. Introduction` 


## B. Family <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)
### `experiment`
Collects data for hyperparameter optimization
<hr width="3%">

### `for_`
Converts data from `experiment` family to plottable data
<hr width="3%">

### `plot`
Plots a static `pyplot` with what is returned from `for_` family

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/PlotFamilyImage.png"   width="700" /> |
|-|
<hr width="3%">

### `interactive`
Plots an interactive `plotly` with what is returned froom `for_` family

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/InteractiveFamilyAni.gif"   width="700" /> |
|-|
<hr width="3%">

### `comparison`
Compares or generates comparison data for two datasets in a `plot`, `interactive`, `DataFrame`, etc.

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/ComparisonFamilyImage.png"   width="700" /> |
|-|


#### Prefixes ####
* `multi`
   * Strictly for plotting, enables comparison of up to five datasets
   
| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/MultiPrefixAni.gif"   width="700" /> |
|-|


* `time_`
   * Meant to represent data from `comparison_Forest` to either a graphical or tabular format
* `opt_`
   * Meant to represent data from `comparison_Forest` to a graphical format
<hr width="3%">

### `optimize`
Finds the parameters of the model that had the lowest mean absolute error with data from the family `experiment`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20XGBR%20Optimized.gif"   width="400" /> |
|-|
<hr width="3%">

### `initialize`
Creates an object specifed in the `Species` based on desired parameters
<hr width="3%">

### `zoom`
Allows for functions in `interactive` family to plot values only below a certain mean absolute error to enhance the granularity of surface plot

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20Magnified%20-%204D%20Surface%20Plot.gif"   width="700" /> |
|-|
<hr width="3%">

## C. Genus <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)  

### Family of `experiment`

#### `_with`
Produces uni or bivariate hyperparameter optimization data depending on species
<hr width="3%">

#### `4D_with`
Produces trivariate hyperparameter optimization data exclusively for an XGB Regressor Model
<hr width="12%">

### Family of `for_`
#### `_3D_plot`
Converts to a plottable 3D data (returns three variables)
<hr width="3%">

#### `_3D_comp`
Converts to a plottable 3D data (returns a dictionary with three variables) meant to simplify the argument syntax for functions that plot multiple surface plots
<hr width="3%">

#### `4D_plot`
Converts to a plottable 4D data (returns a dictionary) and only compatible with `experiment4D_with_XGB`
<hr width="12%">

### Family of `plot`
#### `_wireframe`
Plots a wireframe plot in `pyplot`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/WireframeGenusImage.png"   width="700" /> |
|-|
<hr width="3%">

#### `_surface`
Plots a surface plot in `pyplot`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/PlotFamilyImage.png"   width="700" /> |
|-|
<hr width="12%">




### Family of `interactive`
#### `_surface`
Plots an interactive 3D surface plot in `plotly`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/InteractiveFamilyAni.gif"   width="700" /> |
|-|
<hr width="3%">

#### `_4Dsurface`
Plots an interactive 4D (color being the 4th dimension) surface plot in `plotly`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202-%204D%20Surface%20Plot.gif"   width="700" /> |
|-|
<hr width="12%">


### Family of `comparison`
#### `_Grid_Search`
Performs hyperparamter optimization with `sklearn.model_selection.GridSearchCV` meant for comparison
<hr width="3%">

#### `_plot_surface`
Plots two sets of 3D data in the same `pyplot`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/ComparisonFamilyImage.png"   width="700" /> |
|-|
<hr width="3%">

#### `_interactive_surface`
Plots two sets of 3D data in the same `plotly`

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/FamilyComparisonGenusInteractiveAni.gif"   width="700" /> |
|-|
<hr width="3%">

#### `_to_table`
From prefix of `time_` meant to present data from `comparison_Forest` into a tabular format
<hr width="3%">

#### `_plot`
From prefix of `time_` and `opt_` meant to present data from `comparison_Forest` into a graphical format
| `time_`| 
|--------|
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/plotGenusImage.png"   width="700" />|

<hr width="3%">

| `opt_` |
|--------|
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/PrefixOpt.png"   width="700" />|

<hr width="12%">

### Family of `zoom`
#### `_3D`
Zooms in on 3D data

<hr width="3%">

#### `_4D`
Zooms in on 4D data

<hr width="3%">

#### Without `zoom` vs. With `zoom`
| Result | Input |
|--------|:-------:|
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/InteractiveFamilyAni.gif"   width="700" />|  Without `zoom_3D` | 
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/PrefixZoom3D.gif"   width="700" />| With `zoom_3D` <27000 MAE |
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202-%204D%20Surface%20Plot.gif"   width="700" />|  Without `zoom_4D` |
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20Magnified%20-%204D%20Surface%20Plot.gif"   width="700" />| With `zoom_4D` <25000 MAE |

## D. Species <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)                                                                                         
### Ecosystemic
*Designated based on the ML regressor model used, separated by section often in portfolio, and form ~ 90% of all functions enumerated*
#### `_DT`
* Relates to a Decision Tree Regressor
#### `_Forest`
* Relates to a Random Forest Regressor
#### `_XGB`
* Relates to a XGB Regressor
<hr width="12%">

### Niche
*Describe at most two functions found within ecosystems due to specificity of action*
#### `_plot`
* Plots the data from the function `comparison_Forest` into a line chart
  * Do not confuse with the Family `plot` which deals with 3D plotting
#### `_Pipeline`
* Relates to a Pipeline from `sklearn`
#### `_pipelineCV_Forest`
* Implements the ability to add a `ColumnTransformer` to a Pipeline and specify a number of K-folds to the function `experiment_with_Forest`


## E. Tabular Presentation <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)  
### Table 1. Function Assembly
<table>
<thead>
  <tr>
    <th>Family</th>
    <th>Genus</th>
    <th>Species</th>
    <th>Function Name</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="5"><code>experiment</code></td>
    <td rowspan="4"><code>_with</code></td>
    <td><code>_DT</code></td>
    <td><code>experiment_with_DT</code></td>
  </tr>
  <tr>
    <td><code>_Forest</code></td>
    <td><code>experiment_with_Forest</code></td>
  </tr>
  <tr>
    <td><code>_pipelineCV_Forest</code></td>
    <td><code>experiment_with_pipelineCV_Forest</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>experiment_with_XGB</code></td>
  </tr>
  <tr>
    <td><code>4D_with</code></td>
    <td><code>_XGB</code></td>
    <td><code>experiment4D_with_XGB</code></td>
  </tr>
  <tr>
    <td rowspan="4"><code>for_</code></td>
    <td rowspan="2"><code>3D_plot</code></td>
    <td><code>_Forest</code></td>
    <td><code>for_3D_plot_Forest</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>for_3D_plot_XGB</code></td>
  </tr>
  <tr>
    <td><code>3D_comp</code></td>
    <td><code>_Forest</code></td>
    <td><code>for_3D_comp_Forest</code></td>
  </tr>
  <tr>
    <td><code>4D_plot</code></td>
    <td><code>_XGB</code></td>
    <td><code>for_4D_plot_XGB</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>plot</code></td>
    <td><code>_wireframe</code></td>
    <td><code>_Forest</code></td>
    <td><code>plot_wireframe_Forest</code></td>
  </tr>
  <tr>
    <td><code>_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>plot_surface_Forest</code></td>
  </tr>
  <tr>
    <td rowspan="3"><code>interactive</code></td>
    <td rowspan="2"><code>_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>interactive_surface_Forest</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>interactive_surface_XGB</code></td>
  </tr>
  <tr>
    <td><code>_4Dsurface</code></td>
    <td><code>_XGB</code></td>
    <td><code>interactive_4Dsurface_XGB</code></td>
  </tr>
  <tr>
    <td rowspan="6"><code>comparison</code></td>
    <td><code>_Grid_Search</code></td>
    <td><code>_Forest</code></td>
    <td><code>comparison_Grid_Search_Forest</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>comparison_Forest</code></td>
  </tr>
  <tr>
    <td><code>_plot_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>comparison_plot_surface_Forest</code></td>
  </tr>
  <tr>
    <td><code>_interactive_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>comparison_interactive_surface_Forest</code></td>
  </tr>
  <tr>
    <td><code>_plot_surface</code></td>
    <td><code>_XGB</code></td>
    <td><code>comparison_plot_surface_XGB</code></td>
  </tr>
  <tr>
    <td><code>_interactive_surface</code></td>
    <td><code>_XGB</code></td>
    <td><code>comparison_interactive_surface_XGB</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>multi</code>-<code>comparison</code></td>
    <td><code>plot_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>multicomparison_plot_surface_Forest</code></td>
  </tr>
  <tr>
    <td><code>_interactive_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>multicomparison_interactive_surface_Forest</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>time_</code>-<code>comparison</code></td>
    <td>n/a</td>
    <td><code>_to_table</code></td>
    <td><code>time_comparison_to_table</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_plot</code></td>
    <td><code>time_comparison_plot</code></td>
  </tr>
  <tr>
    <td><code>opt_</code>-<code>comparison</code></td>
    <td>n/a</td>
    <td><code>_plot</code></td>
    <td><code>opt_comparison_plot</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>optimize</code></td>
    <td>n/a</td>
    <td><code>_DT</code></td>
    <td><code>optimize_DT</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>optimize_Forest</code></td>
  </tr>
  <tr>
    <td><code>isDataTable_</code>-<code>optimize</code></td>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>isDataTable_optimize_Forest</code></td>
  </tr>
  <tr>
    <td><code>optimize</code></td>
    <td>n/a</td>
    <td><code>_XGB</code></td>
    <td><code>optimize_XGB</code></td>
  </tr>
  <tr>
    <td rowspan="4"><code>initialize</code></td>
    <td>n/a</td>
    <td><code>_DT</code></td>
    <td><code>initialize_DT</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>initialize_Forest</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Pipeline</code></td>
    <td><code>initialize_Pipeline</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_XGB</code></td>
    <td><code>initialize_XGB</code></td>
  </tr>
  <tr>
    <td rowspan="3"><code>zoom</code></td>
    <td rowspan="2"><code>_3D</code></td>
    <td><code>_Forest</code></td>
    <td><code>zoom_3D_Forest</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>zoom_3D_XGB</code></td>
  </tr>
  <tr>
    <td><code>_4D</code></td>
    <td><code>_XGB</code></td>
    <td><code>zoom_4D_XGB</code></td>
  </tr>
</tbody>
</table>

<hr width="12%">

### Table 2. Function Abbreviation
<table>
<thead>
  <tr>
    <th>Family</th>
    <th>Genus</th>
    <th>Species</th>
    <th>Abbreviation </th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="5"><code>experiment</code></td>
    <td rowspan="4"><code>_with</code></td>
    <td><code>_DT</code></td>
    <td><code>e.w.DT</code></td>
  </tr>
  <tr>
    <td><code>_Forest</code></td>
    <td><code>e.w.Fo</code></td>
  </tr>
  <tr>
    <td><code>_pipelineCV_Forest</code></td>
    <td><code>e.w.pi</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>e.w.XG</code></td>
  </tr>
  <tr>
    <td><code>4D_with</code></td>
    <td><code>_XGB</code></td>
    <td><code>e.4.XG</code></td>
  </tr>
  <tr>
    <td rowspan="4"><code>for_</code></td>
    <td rowspan="2"><code>3D_plot</code></td>
    <td><code>_Forest</code></td>
    <td><code>f.3Dp.Fo</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>f.3.XG</code></td>
  </tr>
  <tr>
    <td><code>3D_comp</code></td>
    <td><code>_Forest</code></td>
    <td><code>f.3Dc.Fo</code></td>
  </tr>
  <tr>
    <td><code>4D_plot</code></td>
    <td><code>_XGB</code></td>
    <td><code>f.4.XG</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>plot</code></td>
    <td><code>_wireframe</code></td>
    <td><code>_Forest</code></td>
    <td><code>p.w.Fo</code></td>
  </tr>
  <tr>
    <td><code>_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>p.s.Fo</code></td>
  </tr>
  <tr>
    <td rowspan="3"><code>interactive</code></td>
    <td rowspan="2"><code>_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>i.s.Fo</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>i.s.XG</code></td>
  </tr>
  <tr>
    <td><code>_4Dsurface</code></td>
    <td><code>_XGB</code></td>
    <td><code>i.4.XG</code></td>
  </tr>
  <tr>
    <td rowspan="6"><code>comparison</code></td>
    <td><code>_Grid_Search</code></td>
    <td><code>_Forest</code></td>
    <td><code>c.G.Fo</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>c.Fo</code></td>
  </tr>
  <tr>
    <td><code>_plot_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>c.p.Fo</code></td>
  </tr>
  <tr>
    <td><code>_interactive_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>c.i.Fo</code></td>
  </tr>
  <tr>
    <td><code>_plot_surface</code></td>
    <td><code>_XGB</code></td>
    <td><code>c.p.XG</code></td>
  </tr>
  <tr>
    <td><code>_interactive_surface</code></td>
    <td><code>_XGB</code></td>
    <td><code>c.i.XG</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>multi</code>-<code>comparison</code></td>
    <td><code>plot_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>m-c.p.Fo</code></td>
  </tr>
  <tr>
    <td><code>_interactive_surface</code></td>
    <td><code>_Forest</code></td>
    <td><code>m-c.i.Fo</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>time_</code>-<code>comparison</code></td>
    <td>n/a</td>
    <td><code>_to_table</code></td>
    <td><code>t-c.to</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_plot</code></td>
    <td><code>t-c.pl</code></td>
  </tr>
  <tr>
    <td><code>opt_</code>-<code>comparison</code></td>
    <td>n/a</td>
    <td><code>_plot</code></td>
    <td><code>o-c.pl</code></td>
  </tr>
  <tr>
    <td rowspan="2"><code>optimize</code></td>
    <td>n/a</td>
    <td><code>_DT</code></td>
    <td><code>o.DT</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>o.Fo</code></td>
  </tr>
  <tr>
    <td><code>isDataTable_</code>-<code>optimize</code></td>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>i-o.Fo</code></td>
  </tr>
  <tr>
    <td><code>optimize</code></td>
    <td>n/a</td>
    <td><code>_XGB</code></td>
    <td><code>o.XG</code></td>
  </tr>
  <tr>
    <td rowspan="4"><code>initialize</code></td>
    <td>n/a</td>
    <td><code>_DT</code></td>
    <td><code>i.DT</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Forest</code></td>
    <td><code>i.Fo</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_Pipeline</code></td>
    <td><code>i.Pi</code></td>
  </tr>
  <tr>
    <td>n/a</td>
    <td><code>_XGB</code></td>
    <td><code>i.XG</code></td>
  </tr>
  <tr>
    <td rowspan="3"><code>zoom</code></td>
    <td rowspan="2"><code>_3D</code></td>
    <td><code>_Forest</code></td>
    <td><code>z.3.Fo</code></td>
  </tr>
  <tr>
    <td><code>_XGB</code></td>
    <td><code>z.3.XG</code></td>
  </tr>
  <tr>
    <td><code>_4D</code></td>
    <td><code>_XGB</code></td>
    <td><code>z.4.XG</code></td>
  </tr>
</tbody>
</table>

<hr width="12%">

### Table 3. Function Purpose
| Function Name                                | Abbreviation  | About                                                                                                                                                                                                                        |
|----------------------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `experiment_with_DT`                         | `e.w.DT`      | *Univariate hyperparameter optimization of Decision Tree Regressor's* `max_leaf_nodes`                                                                                                                                       |
| `experiment_with_Forest`                     | `e.w.Fo`      | *Bivariate hyperparameter optimization of Random Forest Regressor's* `n_estimators` *and* `max_depth`                                                                                                                        |
| `experiment_with_pipelineCV_Forest`          | `e.w.pi`      | *Same optimization as* `experiment_with_Forest` *with the ability to add a* `ColumnTransformer` *preprocessor and specify a number of K-folds*                                                                               |
| `experiment_with_XGB`                        | `e.w.XG`      | *Bivariate hyperparameter optimization of a XGB Regressor's* `n_estimators` *and either* `max_depth` *or* `learning_rate`                                                                                                    |
| `experiment4D_with_XGB`                      | `e.4.XG`      | *Trivariate hyperparameter optimization of a XGB Regressor's* `n_estimators` *,* `max_depth` *, and* `learning_rate`                                                                                                         |
| `for_3D_plot_Forest`                         | `f.3Dp.Fo`    | *Converts the dictionary data from the family* `experiment` *to three two-dimensional matrices (* `max_depth` *,* `mae` *,* `n_estimators` *in that order) that can plotted*                                                 |
| `for_3D_comp_Forest`                         | `f.3Dc.Fo`    | *Converts the dictionary data from the family* `experiment` *into a single dictionary with the three two-dimensional matrices returned in* `for_3D_plot_Forest` *stored as keys*                                             |
| `for_3D_plot_XGB`                            | `f.3.XG`      | *Converts the dictionary data from the family* `experiment` *in same manner as* `for_3D_comp_Forest` *but additional user-inputed boolean* `test_max_depth` *determines whether* `max_depth` *or* `learning_rate` was tested |
| `for_4D_plot_XGB`                            | `f.4.XG`      | *Converts exclusively the dictionary data from* `experiment4D_with_XGB` *into a single dictionary with four two-dimensional matrices that can be plotted together on a 4D surface plot*                                      |
| `plot_wireframe_Forest`                      | `p.w.Fo`      | *Plots data from* `for_3D_plot_Forest` *into a static wireframe plot*                                                                                                                                                        |
| `plot_surface_Forest`                        | `p.s.Fo`      | *Plots data from* `for_3D_plot_Forest` *into a static surface plot*                                                                                                                                                          |
| `interactive_surface_Forest`                 | `i.s.Fo`      | *Plots data from* `for_3D_plot_Forest` *into an interactive surface plot*                                                                                                                                                    |
| `interactive_surface_XGB`                    | `i.s.XG`      | *Plots data from* `for_3D_plot_XGB` *into an interactive surface plot*                                                                                                                                                       |
| `interactive_4Dsurface_XGB`                  | `i.4.XG`      | *Plots data from* `for_4D_plot_Forest` *into an interactive 4D surface plot (with color being the fourth dimension)*                                                                                                         |
| `comparison_Grid_Search_Forest`              | `c.G.Fo`      | *Performs a* `GridSearchCV` *from* `sklearn` *argumentatively-similar to functions in* `experiment` *family*                                                                                                                 |
| `comparison_Forest`                          | `c.Fo`        | *Compares* `GridSearchCV` *optimization to the natively programmed optimization scope of execution time and lowest MAE result; lengthy documentation can be found in the docstring of function*                              |
| `comparison_plot_surface_Forest`             | `c.p.Fo`      | *Plots two datasets from* `for_3D_comp_Forest` *into a single static surface plot*                                                                                                                                           |
| `comparison_interactive_surface_Forest`      | `c.i.Fo`      | *Plots two datasets from* `for_3D_comp_Forest` *into a single interactive surface plot*                                                                                                                                      |
| `comparison_plot_surface_XGB`                | `c.p.XG`      | *Plots two datasets from* `for_3D_comp_Forest` *, which is cross-compatible with* `experiment_with_XGB` *, into a single static surface plot;*                                                                               |
| `comparison_interactive_surface_XGB`         | `c.i.XG`      | *Plots two datasets from* `for_3D_comp_Forest` *, which is cross-compatible with* `experiment_with_XGB` *, into a single interactive surface plot;*                                                                          |
| `multicomparison_plot_surface_Forest`        | `m-c.p.Fo`    | *Plots up to five datasets from* `for_3D_comp_Forest` *into a single static surface plot*                                                                                                                                    |
| `multicomparison_interactive_surface_Forest` | `m-c.i.Fo`    | *Plots up to five datasets from* `for_3D_comp_Forest` *into a single interactive surface plot*                                                                                                                               |
| `time_comparison_to_table`                   | `t-c.to`      | *Converts the first returned variable* `time_results` *from function* `comparison_Forest` *to plottable 2D table data.*                                                                                                      |
| `time_comparison_plot`                       | `t-c.pl`      | *Converts the data from function* `time_comparison_to_table` *to a line chart.*                                                                                                                                              |
| `opt_comparison_plot`                        | `o-c.pl`      | *Converts the second returned variable* `optimization_results` *from function* `comparison_Forest` *to a line chart.*                                                                                                        |
| `optimize_DT`                                | `o.DT`        | *Finds the parameters of the Decision Tree Regressor with the lowest mean absolute error*                                                                                                                                    |
| `optimize_Forest`                            | `o.Fo`        | *Finds the parameters of the Random Forest Regressor with the lowest mean absolute error when* `isDataTable = False` *or unspecified in the argument of* `experiment_with_Forest`                                            |
| `isDataTable_optimize_Forest`                | `i-o.Fo`      | *Finds the parameters of the Random Forest Regressor with the lowest mean absolute error when* `isDataTable = True` *in argument of* `experiment_with_Forest`                                                                |
| `optimize_XGB`                               | `o.XG`        | *Finds the parameters of the XGB Regressor with the lowest mean absolute error. If data is from* `experiment4D_with_XGB`*, then set* `is_4D = True` *in argument.*                                                           |
| `initialize_DT`                              | `i.DT`        | *Initializes a Decision Tree Regressor with desired parameters*                                                                                                                                                              |
| `initialize_Forest`                          | `i.Fo`        | *Initializes a Random Forest Regressor with desired parameters*                                                                                                                                                              |
| `initialize_Pipeline`                        | `i.Pi`        | *Initializes a Pipeline with a given a ML model and preprocessing method (which is a* `ColumnTransformer` *object)*                                                                                                          |
| `initialize_XGB`                             | `i.XG`        | *Initializes a XGB Regressor with desired parameters*                                                                                                                                                                        |
| `zoom_3D_Forest`                             | `z.3.Fo`      | *Allows for* `interactive_surface_Forest` *to plot values only below a certain mean absolute error to enhance the granularity of surface plot*                                                                               |
| `zoom_3D_XGB`                                | `z.3.XG`      | *Allows for* `interactive_surface_XGB` *to plot values only below a certain mean absolute error to enhance the granularity of surface plot*                                                                                  |
| `zoom_4D_XGB`                                | `z.4.XG`      | *Allows for* `interactive_4Dsurface_XGB` *to plot values only below a certain mean absolute error to enhance the granularity of surface plot*                                                                                |
<hr width="12%">

### Table 4. Interactive Master List
#### *Follow these steps to create an interactive/sortable master list with all the aforementioned data:*

### 1) Hold down `⌘ Cmd` or `Ctrl` and click [here](https://docs.google.com/spreadsheets/d/1ICA9vhXx4GZdsE9kFefcVO63GUSXlaC4pbMkB94_r4g/edit?usp=sharing)

<details><summary> Here is the URL if the hyperlink fails:</summary>
<em> https://docs.google.com/spreadsheets/d/1ICA9vhXx4GZdsE9kFefcVO63GUSXlaC4pbMkB94_r4g/edit?usp=sharing </em>
</details>
<hr width="12%">


### 2) Press `⌘ Cmd + A` or `Ctrl + A` and select the filter icon in top left
<hr width="3%">

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Step%202%20Interactive%20Table.gif"   width="800" /> |
|-|

<hr width="12%">

### 3) Click `Create new temporary filter view` and voilà!
<hr width="3%">

| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Step%203%20Interactive%20Table.gif"   width="800" /> |
|-|

## F. Ecosystems <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)

*All the functions within each "ecosystem," a word used to describe a collection of synegistic functions, is enumerated and information about any function can be found in the docstring but will not be presented here. There is no reasoning behind the naming of ecosystems beyond continuing the biologically based paradigm. Also note that biological ecosystems are made up of biotic and abiotic features, whereas all the functions were implicitly biotic features because only those features have classifications in systematics, thus semantically, a more accurate description of this section is not an enumeration of an "Ecosystem" but of all the "biotic factors within an Ecosystem." Some functions here were not included in the functions enumerated and abbreviated in trinomial nomenclature, so perhaps they could be the abiotic factors to an analagously imaginative mind.*
<hr width="12%">

### An Intrasectional Analogical Aside
*The synergy of these ecosystems is not a hard edge but noticeably blended, meaning "inter-ecosystemic" synergy does exist, though a weaker force than the "intra-ecosystemic" synergy; an analogy, chemistry-rooted, would be London Dispersion forces to ionic bonds if one felt so inclined to specify though atomic forces could be considered "holistically analogous" as intramolecular forces are evidently stronger than intermolecular forces. An example of "inter-ecosystem" synergy would be the use of* `for_3D_comp_Forest` *for data produced from* `experiment_with_XGB` *to create a visual comparison of predictiveness between a Random Forest Regressor and XGBR evinced in section* `VI. XG Boost` *and subsection* `B.i.a. Comparison 1`.
<hr width="12%">

### i. Keystone Species
1. `train_model(model_arg, X_arg, y_arg)`

2. `test_model(model_arg, X_arg, y_arg, X_test_arg)`

3. `mae(model_arg, X_arg, y_arg)`
<hr width="12%">

### ii. Decision Tree (Section III)
1. `train_model(model_arg, X_arg, y_arg)`

2. `test_model(model_arg, X_arg, y_arg, X_test_arg)`

3. `mae(model_arg, X_arg, y_arg)`

4. `initialize_DT(max_leaf_nodes_arg)`

5. `experiment_with_DT(max_leaf_nodes_range_arg, X_arg, y_arg, is_data_table = False)`

6. `optimize_DT(max_leaf_nodes_range_arg, X_arg, y_arg)`
<hr width="12%">

### iii. Random Forest (Section IV)
1. `train_model(model_arg, X_arg, y_arg)`

2. `test_model(model_arg, X_arg, y_arg, X_test_arg)`

3. `mae(model_arg, X_arg, y_arg)`

4. `initialize_Forest(n_estimators_arg, max_depth_arg, not_mae=False)`

5. `experiment_with_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, is_data_table = False, NE_increment = 1, percent_complete = False)`

6. `optimize_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, NE_increment_arg = 1)`

7. `for_3D_plot_Forest(experiment_with_Forest_res)`

8. `plot_wireframe_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)`

9. `plot_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)`

10. `interactive_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)`

11. `isDataTable_optimize_Forest(DataTable, n_estimators_range_arg, max_depth_num_or_list_arg, NE_increment_arg = 1)`

12. `comparison_Grid_Search_Forest(n_estimators_arg, max_depth_arg, NE_increment = 1)`

13. `comparison_Forest(n_estimators_range_array_arg, max_depth_range_array_arg, NE_increment_targ = 1, MD_increment_targ = 1)`

14. `time_comparison_to_table(time_comp_arg)`

15. `time_comparison_plot(graph_title, x_axis_arg, time_comp_table_arg, custom_x_axis_title='')`

16. `opt_comparison_plot(graph_title, x_axis_arg, opt_comp_table_arg, custom_x_axis_title='')`

17. `zoom_3D_Forest(max_depth_arg, mae_arg, n_estimators_arg, mae_upper_limit)`
<hr width="12%">

### iv. Random Rainforest - Imputation & Encoding for Forest (Section V)

#### a. Soil Percolation - Imputation (Section V.A)
1. `impute(X_arg, drop_thresh = 2/3)`

2. `comparison_plot_surface_Forest(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                   A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0)`
                                   
3. `comparison_interactive_surface_Forest(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                          A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0)`
                                          
`for_3D_comp_Forest(max_depth_arg, mae_arg, n_estimators_arg)`
<hr width="3%">

#### b. Canopy Percolation - Encoding (Section V.B)
1. `encode(X_train_arg, X_test_arg, cardinality_thresh = 10)`

2. `multicomparison_plot_surface_Forest(title, A_data, B_data, C_data, 
                                        a_alpha = .8, b_alpha = .8, c_alpha = .8,
                                        A_label = '', B_label = '', C_label = '',
                                        a_label_sep = 0, b_label_sep = 0, c_label_sep = 0,
                                        D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0,
                                        E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0)`
                                     
3. `multicomparison_interactive_surface_Forest(title, A_data, B_data, C_data, 
                                               a_alpha = .8, b_alpha = .8, c_alpha = .8,
                                               A_label = '', B_label = '', C_label = '',
                                               a_label_sep = 0, b_label_sep = 0, c_label_sep = 0,
                                               D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0,
                                               E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0)`
<hr width="3%">

#### c. Rain & Weather - Pipeline & K-Fold CV (Section V.C)
1. `mae(model_arg, X_arg, y_arg)`

2. `mae_cross_val(model_arg, X_arg, y_arg, cv_arg = 5)`

3. `initialize_Pipeline(preprocessor_arg, model_arg)`

4. `experiment_with_pipelineCV_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, preprocessor_arg, NE_increment = 1, cv = 5, percent_complete = False)`

5. `average_SD_pipelineCV_Forest(mae_results_sd)`
<hr width="12%">

### v. Mountain - XGB Regressor (Section VI)
1. `experiment4D_with_XGB(n_estimators_range_arg, max_depth_num_or_list_arg, learning_rate_range_arg, X_arg, y_arg, preprocessor_arg, NE_increment = 1, cv = 5, percent_complete = False, learning_rate_divisor = 100)`

2. `for_4D_plot_XGB(experiment_with_XGB_res)`

3. `optimize_XGB(DataTable, is_4D = False, test_max_depth = True)`

4. `comparison_plot_surface_XGB(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                   A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0,
                                   a_xshift = 0, b_xshift = 0)`
                                   
5. `comparison_interactive_surface_XGB(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                       A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0)`
                                       
6. `interactive_4Dsurface_XGB(title, A_data)`                                    

7. `initialize_XGB(n_estimators_arg, learning_rate_arg, max_depth_arg)`

8. `experiment_with_XGB(n_estimators_range_arg, max_depth_or_learning_rate, X_arg, y_arg, preprocessor_arg,
                        NE_increment = 1, cv = 5, percent_complete = False, test_max_depth = True,
                        learning_rate_divisor = 100, default_learning_rate = .1, default_max_depth = 5)`
                        
9. `zoom_4D_XGB(A_data_arg, mae_upper_limit)`

10. `test_model_XGB`

11. `for_3D_plot_XGB(experiment_with_XGB_res, test_max_depth = True)`

12. `interactive_surface_XGB(title, A_data)`

13. `zoom_3D_XGB(A_data_arg, mae_upper_limit)`

## G. Exhibition <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)
***This subsection demonstrates the code implementation of the trinomial nomenclature framework developed in the previous subsections by abbreviating the functions used in subsection*** `A. Demo` ***of*** `I. Introduction` ***.***

### Excerpts & Annotations

*Excerpts (not including code) from* `A. Demo`*, Demo 1.0, Demo, Demo Unabbreviated, or Original Demo will be formatted like the following:*

> Words from the `A. Demo`, Demo 1.0, Demo, Demo Unabbreviated, or Original Demo

*Annotations from* `G. Exhibition`*, Demo 2.0, Demo Abbreviated will be formatted like this.*
* These will above excerpts and will explain the changes

<hr width="3%">

### Demo 2.0

Here, using the `experiment` family, `4D_with` genus, and `_XGB` species, the  function `experiment4D_with_XGB` can be abbreviated to `e4XG` to collect trivariate hyperparameter optimization data.

Additionally, to convert the data into a plottable 4D visualization the function `for_4D_plot_XGB`, which has the family `for_`, genus `4D_plot`, and species `_XGB`, can be used and this abbreviates to `f4XG`. To plot an interactive surface plot, the abbreviation `i4XG` which stands for `interactive_4Dsurface_XGB`, can be used.

> With the following code, you can plot a 4D (color being the 4th dimension) visualization of the hyperparameter optimization for a XGB Regressor Model:

    XGB_4D_e2 = e4XG(200, range(2,7), range(1,101), X_train_pipeline, y, preprocessor, NE_increment=30, cv = 1)
    A_data_4d_e2 = f4XG(XGB_4D_e2)
    i4XG('Experiment 2 with Abbreviated Functions', A_data_4d_e2)

> <details><summary> <em> Curious about the first two lines of code? Click the toggle to learn more: </em></summary> <p> <ul> <li> 200 = Searching from 1 to 200 <code> n_estimators </code> </li> <li> <code> range(2,7)</code>  = Searching from 2 to 6 <code>max_depth</code> </li> <li> <code> range(1,101)</code>  = Searching from .01 to 1 <code> learning_rate</code> </li> <li> <code> X_train_pipeline</code>  = training data </li> <li> <code> y</code>  = actual sale prices  </li> <li> <code> preprocessor</code>  = <code> ColumnTransformer</code>  object that imputes and encodes data </li> <li> <code> NE_increment = 30</code>   = Increments <code> n_estimators</code>  by 30, so instead of 1 to 200, [1, 31, ... 181] </li>  <li> <code> cv = 1</code>  = Number of K-Folds </li> </ul>  </p>
</details>


<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202-%204D%20Surface%20Plot.gif"   width="500" /> 
</p>
<p align="center">
  <em>
    Interactive 4D Plot from Experiment 2 - Section VI XGB Regression
  </em>
</p>

Here, since we want to enlarge the granularity of the graph due to the plateau, we can use the `zoom` family. Since this is a 4D plot, we know to use the genus `_4D` and because this was produced by an `XGBR` we know to use the ecosystemic species `_XGB`. From these deductions we can use the abbreviated function `z4XG` function which is equivalent to `zoom_4D_XGB` to zoom in on the graph:

> Notice how the graph plateaus around mean absolute error (MAE) of 2000. To optimize the model, we want to find the lowest MAE value and the parameters that produced that value. To better observe where this optimal model is let's magnify that portion of the graph to increase the granularity:
    
    A_data_4d_e2_mag = z4XG(A_data_4d_e2, 25000)
    i4XG('Experiment 1 Magnified', A_data_4d_e2_mag)

<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20Magnified%20-%204D%20Surface%20Plot.gif"          width="500" /> 
</p>
<p align="center">
  <em>
    Experiment 2 Magnified (<2500 MAE) - Section VI XGB Regression
  </em>
</p>

To find the optimal parameters, we can we want to use the `optimize` family and because this is an `XBGR` we also know to use the species `_XGB`, thus we find the abbreviated function `oXG` which is equivalent to `optimize_XGB`. However, if this was a `Random Forest Regressor` then we would know to use `oFo` or for a `Decision Tree Regressor` we would know to use `oDT` demonstrating the flexibility and intuitiveness of the system.

> Though we know roughly know what model's optimal parameters should look like, to find the most performant model we can call the `optimize_XGB(...)` function:

<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20Abbreviated%20Magnified%20-%204D%20Surface%20Plot.gif"   width="500" /> 
</p>
<p align="center">
  <em>
    1st argument = data, 2nd argument = classifier (4D will have one more dimension than 3D)
  </em>
</p>

## H. Areas of Improvement <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)

*Like anything in this world, the pursuit of perfection is an asymptote not a loading screen &mdash; though the latter at times may remarkably feel like the former. Here, we briefly discuss systemic and mechanical shortcomings, possible counter claims, and so on; however, I hypothesize all the points enumerated here are but the tip of the iceberg.*

<hr width="12%">

### Trinomial Nomenclature System
#### Counterclaim
Instead of creating this complicated classification system, the easiest solution to lessening the typing burden would simply be to reduce the unabbreviated names and arguments of functions. Though this solution is easy, it overlooks the nature of this section's quest, which is not the simplify but classify. Only from this classification, does abbreviation rather than an oversimplification becomes possible. I fear that the prefix "over" is hard to separate from the simplify, and without this separation, an oversimplification implies a truncation of relevant information, whereas an abbreviation represents an optimization of relevant information. The section aims to achieve the latter without leading to the former.

<hr width="3%">

#### Ambiguity
Although the system works optimally with most functions, with optimally being defined as a each part of classifications and abbreviation being cogent and intuitively-applied, some functions' abbreviations such as `i-o.Fo` which stands for `isDataTable_optimize_Forest` leave a residue of ambiguity counter to the definition "optimally" and the aim to optimize information.

<hr width="3%">

#### Functional vs. Argumentative
All the functions classified in the trinomial nomenclature system were functional names, and more needs to be done in the area of the standardization and abbreviation of the argumentative environment for each function. If we temporarily dismiss the higher of aim of this section for the material comforts of lessening the typing burden and ergo increasing the efficiency, then I suspect that a majority of the typing burden falls not in the typing of functions but rather the typing of these function's arguments. The enjoyable irony of this section is that it discusses a method of "decreasing the typing burden" by a lot of typing.

<hr width="3%">

#### Simplicity
Though the fear of *over*simplication was stated in the `Counterclaim` section, simplification and its attendant characteristic of simplicity should be welcomed like a familiar face returning home. Things were often simple before they were complicated. This system, termed a "Trinomial Nomenclature" to me feels like a regression to the "Binomial Nomenclature" due to its dependence to an extra term for its abbreviation, but perhaps the comparison is unjust. Regardless, though I felt like the system accomplished much in classification and abbreviation, I always felt a simpler, more elegant solution always elusive like Tantalus's fruit was about to be concieved to replace the current system, but alas, one cannot utter the words on the tip of one's tongue and I did not find such system.

<hr width="12%">

### Holistic Section
#### Expository Style
It would be ignorant of me to acknowledge that many sections are explained in a writing style that relies upon intricate setences bordering on Hawthornian syntax that may convolute the sentence's meaning. To address these criticisms, I accept them. My style was more a natural stream of consciousness than a contrived jet stream of eloquence. The latter is what I strive for in works that I design to appeal to larger audience and when the purpose is meant for audience consumption, but the purpose of this writing is more a earnest exploration of my curiosity that so happens to be crystallized in writing here. I will make no effort to change the writing style here but I do acknowledge that deficiencies in the expository style may hinder comprehension.


