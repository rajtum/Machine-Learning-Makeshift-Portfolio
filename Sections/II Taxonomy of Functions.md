# II. Taxonomy of Functions
## Précis
*The premise of this section is to classify and explicate the functions within this portfolio by the looking at the functions through the prism of taxonomy. This section aims to create a logical and intuitive trinomial nomenclature framework, modeled after the binomial nomenclature classification of systematics, for naming and abbreviating of functions within this portfolio, enabling functions such as* `experiment_with_XGB` *to be shortened to* `ewXG` *and* `comparison_plot_surface_XGB` *to* `cpXG`*. None of these abbreviations were used in future sections in case the reader had not familiarized themselves with this section, but all abbreviations are performant and ergo can be used in the coding playground; additionally, to illustrate the implementation of this section, the subsection* `A. Demo` found in the `README.md` at this repository's homepage was recoded with abbreviated functions in subsection `G. Exhibition`.


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
#### &emsp;&emsp; [C. Genus](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#c-genus---point_up_2)

#### &emsp;&emsp; [D. Species](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#d-species---point_up_2)
&emsp;&emsp;&emsp;&emsp; [Ecosystemic](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#ecosystemic)

&emsp;&emsp;&emsp;&emsp; [Niche](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#niche)

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

#### &emsp;&emsp; [G. Exhibition]


## A. Adaptations <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)

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
    * Though irksomely illogical in context of biology taxonomical paradigm which inspired its conception, the rule enables classification of more functions at the sake of introducing a systemics depravity.
  * **Conflict Clause**: In the event that the same abbreviation will be used for two or more distinct functions, then the `Genus` will be appended to these abbreviations one letter at a time until no two functions have the same abbreviation.
    * i.e. `for_3D_plot_Forest` and `for_3D_comp_Forest` respectively become `f.3Dp.Fo` and `f.3Dc.Fo`
  * **Hypothetical but Extended Conflict Clause**: Although no instance occurs where the aforementioned conflict clause enumerating the `Genus` letter by letter does not fail to distinguish multiple function's abbreviations, if such example were to occur theoretically, then the `Family`, `Species`, and `Prefix` in that order would be enumerated in the same fashion until the same aim of unique abbreviations for each function is accomplished. This rule would most likely be called upon in circumstances where there is the function has no `Genus` and would ergo seldom apply.
* **Coding Implementation:**
  * Equivalent functions will be available in both the abbreviated and unabbreviated in the coding environment, but only the unabbreviated versions will be used in section in case the reader has not familiarized themselves with this section.
  * The abbreviated function name retains all the capitalization but the period mark demarcating classification rank will be removed
    * i.e. The abbreviation `f.3Dp.Fo` (returns 3D plottable dictionary data) or `e.w.XG` (bivariate hyperparamter optimization of XGBR) become respectively `f3DpFo(...)` and `ewXG(...)` and are equivalent to the corresponding functions `for_3D_comp_Forest` and `experiment_with_XGB`
  * Since no abbreviated functions were used in future sections, a exhibition of this section's contributions can 


## B. Family <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)
### `experiment`
Collects data for hyperparameter optimization
<hr width="3%">

### `for_`
Converts data from `experiment` family to plottable data
<hr width="3%">

### `plot`
Plots a static `pyplot` with what is returned from `for_` family
<hr width="3%">

### `interactive`
Plots an interactive `plotly` with what is returned froom `for_` family
<hr width="3%">

### `comparison`
Compares or generates comparison data for two datasets in a `plot`, `interactive`, `DataFrame`, etc.

**Prefixes**
* `multi`
   * Strictly for plotting, enables comparison of up to five datasets
* `time_`
   * Meant to represent data from `comparison_Forest` to either a graphical or tabular format
* `opt_`
   * Meant to represent data from `comparison_Forest` to a graphical format
<hr width="3%">

### `optimize`
Finds the parameters of the model that had the lowest mean absolute error with data from the family `experiment`
<hr width="3%">

### `initialize`
Creates an object specifed in the `Species` based on desired parameters
<hr width="3%">

### `zoom`
Allows for functions in * `interactive` *family to plot values only below a certain mean absolute error to enhance the granularity of surface plot*

## C. Genus <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)  

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

#### `4D_comp`
Converts to a plottable 4D data (returns a dictionary) and only compatible with `experiment4D_with_XGB`
<hr width="12%">

### Family of `plot`
#### `_wireframe`
Plots a wireframe plot in `pyplot`
<hr width="3%">

#### `_surface`
Plots a surface plot in `pyplot`
<hr width="12%">

### Family of `interactive`
#### `_surface`
Plots an interactive 3D surface plot in `plotly`
<hr width="3%">

#### `_4Dsurface`
Plots an interactive 4D (color being the 4th dimension) surface plot in `plotly`
<hr width="12%">

### Family of `comparison`
#### `_Grid_Search`
Performs hyperparamter optimization with `sklearn.model_selection.GridSearchCV` meant for comparison
<hr width="3%">

#### `_plot_surface`
Plots two sets of 3D data in the same `pyplot`
<hr width="3%">

#### `_interactive_surface`
Plots two sets of 3D data in the same `plotly`
<hr width="3%">

#### `_to_table`
From prefix of `time_` meant to present data from `comparison_Forest` into a tabular format
<hr width="3%">

#### `_plot`
From prefix of `time_` and `opt_` meant to present data from `comparison_Forest` into a graphical format
<hr width="12%">

### Family of `zoom`
#### `_3D`
Zooms in on 3D data
<hr width="3%">

#### `_4D`
Zooms in on 4D data


## D. Species <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)                                                                                         
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


## E. Tabular Presentation <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)  
### Table 1. Function Assembly
| Family                    | Genus                  | Species              | Function Name                                |
|---------------------------|------------------------|----------------------|----------------------------------------------|
| `experiment`              | `_with`                | `_DT`                | `experiment_with_DT`                         |
| `experiment`              | `_with`                | `_Forest`            | `experiment_with_Forest`                     |
| `experiment`              | `_with`                | `_pipelineCV_Forest` | `experiment_with_pipelineCV_Forest`          |
| `experiment`              | `_with`                | `_XGB`               | `experiment_with_XGB`                        |
| `experiment`              | `4D_with`              | `_XGB`               | `experiment4D_with_XGB`                      |
| `for_`                    | `3D_plot`              | `_Forest`            | `for_3D_plot_Forest`                         |
| `for_`                    | `3D_comp`              | `_Forest`            | `for_3D_comp_Forest`                         |
| `for_`                    | `3D_plot`              | `_XGB`               | `for_3D_plot_XGB`                            |
| `for_`                    | `4D_plot`              | `_XGB`               | `for_4D_plot_XGB`                            |
| `plot`                    | `_wireframe`           | `_Forest`            | `plot_wireframe_Forest`                      |
| `plot`                    | `_surface`             | `_Forest`            | `plot_surface_Forest`                        |
| `interactive`             | `_surface`             | `_Forest`            | `interactive_surface_Forest`                 |
| `interactive`             | `_surface`             | `_XGB`               | `interactive_surface_XGB`                    |
| `interactive`             | `_4Dsurface`           | `_XGB`               | `interactive_4Dsurface_XGB`                  |
| `comparison`              | `_Grid_Search`         | `_Forest`            | `comparison_Grid_Search_Forest`              |
| `comparison`              | n/a                    | `_Forest`            | `comparison_Forest`                          |
| `comparison`              | `_plot_surface`        | `_Forest`            | `comparison_plot_surface_Forest`             |
| `comparison`              | `_interactive_surface` | `_Forest`            | `comparison_interactive_surface_Forest`      |
| `comparison`              | `_plot_surface`        | `_XGB`               | `comparison_plot_surface_XGB`                |
| `comparison`              | `_interactive_surface` | `_XGB`               | `comparison_interactive_surface_XGB`         |
| `multi`-`comparison`      | `plot_surface`         | `_Forest`            | `multicomparison_plot_surface_Forest`        |
| `multi`-`comparison`      | `_interactive_surface` | `_Forest`            | `multicomparison_interactive_surface_Forest` |
| `time_`-`comparison`      | n/a                    | `_to_table`          | `time_comparison_to_table`                   |
| `time_`-`comparison`      | n/a                    | `_plot`              | `time_comparison_plot`                       |
| `opt_`-`comparison`       | n/a                    | `_plot`              | `opt_comparison_plot`                        |
| `optimize`                | n/a                    | `_DT`                | `optimize_DT`                                |
| `optimize`                | n/a                    | `_Forest`            | `optimize_Forest`                            |
| `isDataTable_`-`optimize` | n/a                    | `_Forest`            | `isDataTable_optimize_Forest`                |
| `optimize`                | n/a                    | `_XGB`               | `optimize_XGB`                               |
| `initialize`              | n/a                    | `_DT`                | `initialize_DT`                              |
| `initialize`              | n/a                    | `_Forest`            | `initialize_Forest`                          |
| `initialize`              | n/a                    | `_Pipeline`          | `initialize_Pipeline`                        |
| `initialize`              | n/a                    | `_XGB`               | `initialize_XGB`                             |
| `zoom`                    | `_3D`                  | `_Forest`            | `zoom_3D_Forest`                             |
| `zoom`                    | `_3D`                  | `_XGB`               | `zoom_3D_XGB`                                |
| `zoom`                    | `_4D`                  | `_XGB`               | `zoom_4D_XGB`                                |
<hr width="12%">

### Table 2. Function Abbreviation
| Family                    | Genus                  | Species              | Abbreviation  |
|---------------------------|------------------------|----------------------|---------------|
| `experiment`              | `_with`                | `_DT`                | `e.w.DT`      |
| `experiment`              | `_with`                | `_Forest`            | `e.w.Fo`      |
| `experiment`              | `_with`                | `_pipelineCV_Forest` | `e.w.pi`      |
| `experiment`              | `_with`                | `_XGB`               | `e.w.XG`      |
| `experiment`              | `4D_with`              | `_XGB`               | `e.4.XG`      |
| `for_`                    | `3D_plot`              | `_Forest`            | `f.3Dp.Fo`    |
| `for_`                    | `3D_comp`              | `_Forest`            | `f.3Dc.Fo`    |
| `for_`                    | `3D_plot`              | `_XGB`               | `f.3.XG`      |
| `for_`                    | `4D_plot`              | `_XGB`               | `f.4.XG`      |
| `plot`                    | `_wireframe`           | `_Forest`            | `p.w.Fo`      |
| `plot`                    | `_surface`             | `_Forest`            | `p.s.Fo`      |
| `interactive`             | `_surface`             | `_Forest`            | `i.s.Fo`      |
| `interactive`             | `_surface`             | `_XGB`               | `i.s.XG`      |
| `interactive`             | `_4Dsurface`           | `_XGB`               | `i.4.XG`      |
| `comparison`              | `_Grid_Search`         | `_Forest`            | `c.G.Fo`      |
| `comparison`              | n/a                    | `_Forest`            | `c.Fo`        |
| `comparison`              | `_plot_surface`        | `_Forest`            | `c.p.Fo`      |
| `comparison`              | `_interactive_surface` | `_Forest`            | `c.i.Fo`      |
| `comparison`              | `_plot_surface`        | `_XGB`               | `c.p.XG`      |
| `comparison`              | `_interactive_surface` | `_XGB`               | `c.i.XG`      |
| `multi`-`comparison`      | `plot_surface`         | `_Forest`            | `m-c.p.Fo`    |
| `multi`-`comparison`      | `_interactive_surface` | `_Forest`            | `m-c.i.Fo`    |
| `time_`-`comparison`      | n/a                    | `_to_table`          | `t-c.to`      |
| `time_`-`comparison`      | n/a                    | `_plot`              | `t-c.pl`      |
| `opt_`-`comparison`       | n/a                    | `_plot`              | `o-c.pl`      |
| `optimize`                | n/a                    | `_DT`                | `o.DT`        |
| `optimize`                | n/a                    | `_Forest`            | `o.Fo`        |
| `isDataTable_`-`optimize` | n/a                    | `_Forest`            | `i-o.Fo`      |
| `optimize`                | n/a                    | `_XGB`               | `o.XG`        |
| `initialize`              | n/a                    | `_DT`                | `i.DT`        |
| `initialize`              | n/a                    | `_Forest`            | `i.Fo`        |
| `initialize`              | n/a                    | `_Pipeline`          | `i.Pi`        |
| `initialize`              | n/a                    | `_XGB`               | `i.XG`        |
| `zoom`                    | `_3D`                  | `_Forest`            | `z.3.Fo`      |
| `zoom`                    | `_3D`                  | `_XGB`               | `z.3.XG`      |
| `zoom`                    | `_4D`                  | `_XGB`               | `z.4.XG`      |
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
<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Step%202%20Interactive%20Table.gif"   width="800" />
<hr width="12%">

### 3) Click `Create new temporary filter view` and voilà!
<hr width="3%">
<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Step%203%20Interactive%20Table.gif"   width="800" />


## F. Ecosystems <!-- Below is an inelegant, verbose, unadaptive improvisation to flush text to right (\hfill in latex) since Github Markdown blocks CSS for security reasons --> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:point_up_2:](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#table-of-contents)

*All the functions within each "ecosystem," a word used to describe a collection of synegistic functions, is enumerated and information about any function can be found in the docstring but will not presented here. There is no reasoning behind the naming of ecosystems beyond continuing the biologically based paradigm. Also note the comparison comes up short as biological ecosystems are made up of biotic and abiotic features, whereas all the functions were implicitly biotic features because only those features have classifications in systematics.*
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

3. `optimize_XGB(DataTable, is_4D = False)`

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
