# II. Taxonomy of Functions
## Précis
*The method of documentation presented in this section is more a creative flourish than an essential read. Conventional documentation can be found on any method below with the* `help` *command or in the function's code as docstring and commented code. The premise of this section is to seek to classify and explicate the functions within this portfolio by the looking at the functions through the prism of taxonomy.*

*Please note in biological taxonomic classifications, only the genus (first letter capitalized) and species (not capitalized) is italicized to identify an organism in a system called binomial nomeclature. Here, trinomial nomenclature with adapted classifications, format typography, and abbreviations will be used to classify and explicate functions and attendant "ecosystems." Function "ecosystems" represented a group of functions that worked in a synergistic fashion and each section of code within this portfolio was designated its own "ecosystem." While a whimsical liberty was taken in the naming of "ecosystems," some more apropos than others, these names should not be impediment to comprehension and do not serve any special purpose beyond continuing the environmental-taxonomical biologist lens of expounding. This is not an exhuastive list of all functions but rather a strategic collection of functions that may be most confusing at first glance and/or with synergistic functionality.*
## Table of Contents
### II. Taxonomy of Functions
#### [A. Adaptations](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#a-adaptations-1)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [i. Classifications](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#i-classifications)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ii. Format Typography](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#ii-format-typography)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [iii. Abbreviation](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#iii-abbreviation)

#### [B. Family](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#b-family-1)
#### [C. Genus](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#c-genus-1)
#### [D. Species](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#d-species-1)
#### [E. Ecosystems](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md#e-ecosystems-1)
## A. Adaptations

### i. Classifications
* `Family Genus Species`
  * Some families have *prefices* in addition to the root name
    * For instance, within the family `comparison`, there are the three prefixes `time_`, `opt_`, and `multi`, which can be concatenated
* Trinomial Nomenclature
### ii. Format Typography
* Will not be italicized
* Will be formatted as code like this: `code`
* Capitalization will be determined by the individual names rather than collective ranks
### iii. Abbreviation
* Will not follow *Genus species* becomes *G. species*
* Instead, `Family Genus Species` becomes `F.G.Species`
  * Note capitalization will follow rule declared in typography
    * i.e. `Family genus SPECIES` becomes `F.g.SPECIES`
  * Underscores and special characters will be ignored in this
    * i.e. only the first letter will be used in abbreviation
    
## B. Family

### `experiment`
* Collects data for hyperparameter optimization
### `for_`
* Converts data from `experiment` family to plottable data
### `plot`
* Plots a static `pyplot` with what is returned from `for_` family
### `interactive`
* Plots an interactive `plotly` with what is returned froom `for_` family
### `comparison`
* Compares or generates comparison data for two datasets in a `plot`, `interactive`, `DataFrame`, etc.
* There are three prefices which modify the family's function:
#### Prefices 
`multi`
* Strictly for plotting, enables comparison of up to five datasets

`time_`
* Meant to represent data from `comparison_Forest` to either a graphical or tabular format

`opt_`
* Meant to represent data from `comparison_Forest` to a graphical format

## C. Genus

### Family of `experiment`

#### `_with`
* Produces uni or bivariate hyperparameter optimization data depending on species
#### `4D_with`
* Produces trivariate hyperparameter optimization data exclusively for an XGB Regressor Model
---
### Family of `for_`
#### `_3D_plot`
* Converts to a plottable 3D data (returns three variables)
#### `_3D_comp`
* Converts to a plottable 3D data (returns a dictionary with three variables) meant to simplify the argument syntax for functions that plot multiple surface plots
#### `4D_comp`
* Converts to a plottable 4D data (returns a dictionary) and only compatible with `experiment4D_with_XGB`
---
### Family of `plot`
#### `_wireframe`
* Plots a wireframe plot in `pyplot`
#### `_surface`
* Plots a surface plot in `pyplot`
---
### Family of `interactive`
#### `_surface`
* Plots an interactive 3D surface plot in `plotly`
#### `_4Dsurface`
* Plots an interactive 4D (color being the 4th dimension) surface plot in `plotly`
---
### Family of `comparison`
#### `_Grid_Search`
* Performs hyperparamter optimization with `sklearn.model_selection.GridSearchCV` meant for comparison
#### `_plot_surface`
* Plots two sets of 3D data in the same `pyplot`
#### `_interactive_surface`
* Plots two sets of 3D data in the same `plotly`
#### `_to_table`
* From prefix of `time_` meant to present data from `comparison_Forest` into a tabular format
#### `_plot`
* From prefix of `time_` and `opt_` meant to present data from `comparison_Forest` into a graphical format


## D. Species
| Family               | Genus          | Species              | Function Name                         | About                                                                                                                                                                                   |
|----------------------|----------------|----------------------|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `experiment`         | `_with`        | `_DT`                | `experiment_with_DT`                  | *Univariate hyperparameter optimization of Decision Tree Regressor's* `max_leaf_nodes`                                                                                                  |
| `experiment`         | `_with`        | `_Forest`            | `experiment_with_Forest`              | *Bivariate hyperparameter optimization of Random Forest Regressor's* `n_estimators` *and* `max_depth`                                                                                   |
| `experiment`         | `_with`        | `_pipelineCV_Forest` | `experiment_with_pipelineCV_Forest`   | *Same optimization as* `experiment_with_Forest` *with the ability to add a* `ColumnTransformer` *preprocessor and specify a number of K-folds*                                          |
| `experiment`         | `_with`        | `_XGB`               | `experiment_with_XGB`                 | *Bivariate hyperparameter optimization of a XGB Regressor's* `n_estimators` *and either* `max_depth` *or* `learning_rate`                                                               |
| `experiment`         | `4D_with`      | `_XGB`               | `experiment4D_with_XGB`               | *Trivariate hyperparameter optimization of a XGB Regressor's* `n_estimators` *,* `max_depth` *, and* `learning_rate`                                                                    |
| `for_`               | `3D_plot`      | `_Forest`            | `for_3D_plot_Forest`                  | *Converts the dictionary data from the family* `experiment` *to three two-dimensional matrices (* `max_depth` *,* `mae` *,* `n_estimators` *in that order) that can plotted*            |
| `for_`               | `3D_comp`      | `_Forest`            | `for_3D_comp_Forest`                  | *Converts the dictionary data from the family* `experiment` *into a single dictionary with the three two-dimensional matrices returned in* `for_3D_plot_Forest` *stored as keys*        |
| `for_`               | `4D_plot`      | `_XGB`               | `for_4D_plot_Forest`                  | *Converts exclusively the dictionary data from* `experiment4D_with_XGB` *into a single dictionary with four two-dimensional matrices that can be plotted together on a 4D surface plot* |
| `plot`               | `_wireframe`   | `_Forest`            | `plot_wireframe_Forest`               | *Plots data from* `for_3D_plot_Forest` *into a static wireframe plot*                                                                                                                   |
| `plot`               | `_surface`     | `_Forest`            | `plot_surface_Forest`                 | *Plots data from* `for_3D_plot_Forest` *into a static surface plot*                                                                                                                     |
| `interactive`        | `_surface`     | `_Forest`            | `interactive_surface_Forest`          | *Plots data from* `for_3D_plot_Forest` *into an interactive surface plot*                                                                                                               |
| `interactive`        | `_4Dsurface`   | `_XGB`               | `interactive_4Dsurface_XGB`           | *Plots data from* `for_4D_plot_Forest` *into an interactive 4D surface plot (with color being the fourth dimension)*                                                                    |
| `comparison`         | `_Grid_Search` | `_Forest`            | `comparison_Grid_Search_Forest`       |                                                                                                                                                                                         |
| `comparison`         |                |                      |                                       |                                                                                                                                                                                         |
| `comparison`         |                |                      |                                       |                                                                                                                                                                                         |
| `comparison`         |                |                      |                                       |                                                                                                                                                                                         |
| `comparison`         |                |                      |                                       |                                                                                                                                                                                         |
| `comparison`         |                |                      |                                       |                                                                                                                                                                                         |
|                      |                |                      |                                       |                                                                                                                                                                                         |
|                      |                |                      |                                       |                                                                                                                                                                                         |
|                      |                |                      |                                       |                                                                                                                                                                                         |
|                      |                |                      |                                       |                                                                                                                                                                                         |
|                      |                |                      |                                       |                                                                                                                                                                                         |
| `multi`-`comparison` | `plot_surface` | `_Forest`            | `multicomparison_plot_surface_Forest` | *Plots up to five datasets from* `for_3D_comp_Forest` *into a single static surface plot*                                                                                               |

## E. Ecosystems
### Keystone Species
`train_model(model_arg, X_arg, y_arg)`
`test_model(model_arg, X_arg, y_arg, X_test_arg)`
`mae(model_arg, X_arg, y_arg)`
### Decision Tree (Section III)
`train_model(model_arg, X_arg, y_arg)`
`test_model(model_arg, X_arg, y_arg, X_test_arg)`
`mae(model_arg, X_arg, y_arg)`
`initialize_DT(max_leaf_nodes_arg)`
`experiment_with_DT(max_leaf_nodes_range_arg, X_arg, y_arg, is_data_table = False)`
`optimize_DT(max_leaf_nodes_range_arg, X_arg, y_arg)`
### Forest (Section IV)
`train_model(model_arg, X_arg, y_arg)`
`test_model(model_arg, X_arg, y_arg, X_test_arg)`
`mae(model_arg, X_arg, y_arg)`
`initialize_Forest(n_estimators_arg, max_depth_arg, not_mae=False)`
`experiment_with_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, is_data_table = False, NE_increment = 1, percent_complete = False)`
`optimize_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, NE_increment_arg = 1)`
`for_3D_plot_Forest(experiment_with_Forest_res)`
`plot_wireframe_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)`
`plot_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)`
`interactive_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)`
`isDataTable_optimize_Forest(DataTable, n_estimators_range_arg, max_depth_num_or_list_arg, NE_increment_arg = 1)`
`comparison_Grid_Search_Forest(n_estimators_arg, max_depth_arg, NE_increment = 1)`
`comparison_Forest(n_estimators_range_array_arg, max_depth_range_array_arg, NE_increment_targ = 1, MD_increment_targ = 1)`
`time_comparison_to_table(time_comp_arg)`
`time_comparison_plot(graph_title, x_axis_arg, time_comp_table_arg, custom_x_axis_title='')`
`opt_comparison_plot(graph_title, x_axis_arg, opt_comp_table_arg, custom_x_axis_title='')`
### Rainforest - Imputation & Encoding for Forest (Section V)

#### Soil Percolation - Imputation (Section V.A)
`impute(X_arg, drop_thresh = 2/3)`
`comparison_plot_surface_Forest(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                   A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0)`
`comparison_interactive_surface_Forest(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                          A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0)`
`for_3D_comp_Forest(max_depth_arg, mae_arg, n_estimators_arg)`
#### Canopy Percolation - Encoding (Section V.B)
`encode(X_train_arg, X_test_arg, cardinality_thresh = 10)`
`multicomparison_plot_surface_Forest(title, A_data, B_data, C_data, 
                                        a_alpha = .8, b_alpha = .8, c_alpha = .8,
                                        A_label = '', B_label = '', C_label = '',
                                        a_label_sep = 0, b_label_sep = 0, c_label_sep = 0,
                                        D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0,
                                        E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0)`
`multicomparison_interactive_surface_Forest(title, A_data, B_data, C_data, 
                                               a_alpha = .8, b_alpha = .8, c_alpha = .8,
                                               A_label = '', B_label = '', C_label = '',
                                               a_label_sep = 0, b_label_sep = 0, c_label_sep = 0,
                                               D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0,
                                               E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0)`         
#### Rain & Weather - Pipeline & K-Fold CV (Section V.C)
`mae(model_arg, X_arg, y_arg)`
`mae_cross_val(model_arg, X_arg, y_arg, cv_arg = 5)`
`initialize_Pipeline(preprocessor_arg, model_arg)`
`experiment_with_pipelineCV_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, preprocessor_arg, NE_increment = 1, cv = 5, percent_complete = False)`
`average_SD_pipelineCV_Forest(mae_results_sd)`
### Mountain - XGB Regressor (Section VI)
`experiment4D_with_XGB(n_estimators_range_arg, max_depth_num_or_list_arg, learning_rate_range_arg, X_arg, y_arg, preprocessor_arg, NE_increment = 1, cv = 5, percent_complete = False, learning_rate_divisor = 100)`
`for_4D_plot_XGB(experiment_with_XGB_res)`
`optimize_XGB(DataTable, is_4D = False)`
`comparison_plot_surface_XGB(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                   A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0,
                                   a_xshift = 0, b_xshift = 0)`
`comparison_interactive_surface_XGB(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                       A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0)`
`interactive_4Dsurface_XGB(title, A_data)`                                       
`initialize_XGB(n_estimators_arg, learning_rate_arg, max_depth_arg)`
`experiment_with_XGB(n_estimators_range_arg, max_depth_or_learning_rate, X_arg, y_arg, preprocessor_arg,
                        NE_increment = 1, cv = 5, percent_complete = False, test_max_depth = True,
                        learning_rate_divisor = 100, default_learning_rate = .1, default_max_depth = 5)`
`zoom_4D_XGB(A_data_arg, mae_upper_limit)`
`test_model_XGB`