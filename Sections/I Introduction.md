# I. Introduction

## Author's Note

This "Machine Learning Makeshift Portfolio" was initially conceived to be as it is titled, a makeshift to demonstrate my proficiency in coding machine learning models; something short and quick, but nonetheless demonstrating. However, as I am finishing this project, I realize curiosity took the reigns of pragmatism's chariot and the project drifted far from the purpose of its conception with Section II eccentrically and probably too thouroughly propounding a trinomial nomenclature framework for classifying functions or Section IV's spritied but flawed comparison of the optimization function programmed with `GridSearchCV` optimization from `sklearn` or the 4D graphical representation of trivariate hyperparameter optimization for an XGBR which sounds ostensibly impressive until learning the fourth dimension is simply color. Though I know I have slightly belittled what I have made in prior sentence, make no mistake, I enjoyed every second of this intellectual voyage despite arriving at a different destination. 

I hope you find something of value in this different destination. Feel free to explore whatever interests you.

## A. Demo

With the following code, you can plot a 4D (color being the 4th dimension) visualization of the hyperparameter optimization for a XGB Regressor Model:

    XGB_4D_e2 = experiment4D_with_XGB(200, range(2,7), range(1,101), X_train_pipeline, y, 
                                      preprocessor, NE_increment=30, cv = 1)
    A_data_4d_e2 = for_4D_plot_XGB(XGB_4D_e2)
    interactive_4Dsurface_XGB('Experiment 2', A_data_4d_e2)
    
<details><summary> <em> Curious about the first two lines of code? Click the toggle to learn more: </em></summary>
<p>
    
 * 200 = Searching from 1 to 200 `n_estimators`
 * `range(2,7)` = Searching from 2 to 6 `max_depth`
 * `range(1,101)` = Searching from .01 to 1 `learning_rate`
 * `X_train_pipeline` = training data
 * `y` = actual sale prices
 * `preprocessor` = `ColumnTransformer` object that imputes and encodes data
 * `NE_increment = 30`  = Increments `n_estimators` by 30, so instead of 1 to 200, [1, 31, ... 181]
 * `cv = 1` = Number of K-Folds
 
</p>
</details>

<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202-%204D%20Surface%20Plot.gif"   width="500" /> 
</p>
<p align="center">
  <em>
    Interactive 4D Plot from Experiment 2 - Section VI XGB Regression
  </em>
</p>
 
Notice how the graph plateaus around mean absolute error (MAE) of 2000. To optimize the model, we want to find the lowest MAE value and the parameters that produced that value. To better observe where this optimal model is let's magnify that portion of the graph to increase the granularity:
    
    A_data_4d_e2_mag = zoom_4D_XGB(A_data_4d_e2, 25000)
    interactive_4Dsurface_XGB('Experiment 1 Magnified', A_data_4d_e2_mag)

<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20Magnified%20-%204D%20Surface%20Plot.gif"          width="500" /> 
</p>
<p align="center">
  <em>
    Experiment 2 Magnified (<2500 MAE) - Section VI XGB Regression
  </em>
</p>

Though we know roughly know what model's optimal parameters should look like, to find the most performant model we can call the `optimize_XGB(...)` function:

<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20XGBR%20Optimized.gif"   width="500" /> 
</p>
<p align="center">
  <em>
    1st argument = data, 2nd argument = classifier (4D will have one more dimension than 3D)
  </em>
</p>


## B. About
The purpose of this portfolio is to (1) *evince* my ability to code machine learning (ML) models, (2) *showcase* my style of computative research, and most importantly, (3) to *politely shout out from the rooftops* my passion for machine learning. In this project, the Ames Housing Dataset, compiled in this [scientific paper](http://jse.amstat.org/v19n3/decock.pdf) by Dean De Cock, was used to build ML models that predict the sale price of houses. Both the training and testing datasets downloaded from Kaggle can be found in the `data` folder as `train_data.csv` and `test_data.csv`. The barometer of the model's predictiveness was mean absolute error (MAE), which measures how model's predictions differ from the actual values; in this case, the MAE represents the arithmetic proximity of the model's predicted sale prices of houses in Ames, Iowa to the actual sale prices of these houses in U.S. dollars. For instance, the optimized model above was able to predict sale prices of houses within $15,000.

## C. Structure
The portfolio is broken up into the following structure:

### [`I. Introduction.md`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/I%20Introduction.md)
    
   * Crystalizes the main highlights of the portfolio and acts as a compass for a person navigating through the portoflio

<hr width = "3%">

### [`II Taxonomy of Functions.md`](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md)
    
   * Offers an evolutionary biologist overview for "family" of functions as an additional source of documentation in addition to the `help(...)` function that can be called for any function
   * Trinomial Nomenclature with adapted typography, classification ranks, and abbreviation rules enabled the creation of logical and intuitive shorthand for coding functions within portfolio
   
<details><summary> Trinomial Nomenclature of Functions (Table 2 & 3 from Section <a href="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md"><code> II Taxonomy of Functions.md </code></a>)   </summary>

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

</details>

<hr width = "3%">
    
### [`III Decision Tree Regression.ipynb`](https://colab.research.google.com/drive/1q2WktD37RdSJzF2eTMzsMa8wdAQdwri1?usp=sharing)

   * Defines a family of functions for univariable hyperparameter optimization of the decision tree's max number of leaf nodes ( `max_leaf_nodes` ) in a Decision Tree Regressor from `sklearn.tree`
<hr width = "3%">
 
### [`IV Random Forest Regression.ipynb`](https://colab.research.google.com/drive/1VgqSp3BSiRJeZZWfxzLEkD7xe6EWQ_f1?usp=sharing)

   * Defines an family of functions for multivariable hyperparameter optimization of the number of trees ( `n_estimators` ) and max depth of each tree ( `max_depth` ) in a Random Forest Regressor from `sklearn.ensemble`
   * Enables a visualization of results in an interactive 3D surface plot, the ability to produce these interactive results with a minimal coding background, and four experimental presets to expound the designed use of functions
   
| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/InteractiveFamilyAni.gif"   width="700" /> |
|-|

   * Compares the programmed hyperparamter optimization function to the public `GridSearchCV` from `sklearn.model_selection` in two areas: (1) speed of optimization program and (2) accuracy of optimization program
   
| <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/PrefixOpt.png"   width="700" /> |
|-|
   
<hr width = "3%">
 
### [`V Add More Predictors.ipynb`](https://colab.research.google.com/drive/1V8bdK2vUBGASpOIfo_-K7-iNbOVAiPmh?usp=sharing)
 
   * Creates functions for imputation, encoding, pipeline, and cross-validation that are compatible with hyperparamter optimization and visualization functions derived in the above section
   * Extends graphing capabilities of previous functions to enable the juxtaposition of multiple datasets in an interactive 3D surface plot
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/MultiPrefixAni.gif"   width="500" />|
|-|
<hr width = "3%">
 
### [`VI XGB Regression.ipynb`](https://colab.research.google.com/drive/1VbZ3RL22IGlTu3wydawMK0SQwMkIuomQ?usp=sharing)

   * Extends the capabiility for the family of functions devised in Section IV to trivariate hyperparameter optimization and 4D graphical capabilites (color being the fourth dimension) to optimize and visualize how the number of trees ( `n_estimators` ), max depth of each tree ( `max_depth` ), and learning rate ( `learning_rate` ) influences model predictiveness
   
| Without `zoom` function | With `zoom` function |
|-------------------------|----------------------|
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%203%20-%204D%20Surface%20Plot.gif"   width="500" />|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%203%20Magnified%20-%204D%20Surface%20Plot.gif"   width="500" />| 

   * Maintains the bivariate hyperparameter optimization compatibility in the genus `experiment(...)` and `optimize(...)` developed in previous sections
<hr width = "3%">
