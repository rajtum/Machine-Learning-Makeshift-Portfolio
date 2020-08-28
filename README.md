# I. Introduction
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

### I. Introduction (What you are reading now)
    
   * Crystalizes the main highlights of the portfolio and acts as a compass for a person navigating through the portoflio
  
### II. Taxonomy of Functions
    
   * Offers an evolutionary biologist overview for "family" of functions as an additional source of documentation in addition to the `help(...)` function that can be called for any function
    
### III. Decision Tree Regression

   * Defines a family of functions for univariable hyperparameter optimization of the decision tree's max number of leaf nodes ( `max_leaf_nodes` ) in a Decision Tree Regressor from `sklearn.tree`
 
### IV. Random Forest Regression

   * Defines an family of functions for multivariable hyperparameter optimization of the number of trees ( `n_estimators` ) and max depth of each tree ( `max_depth` ) in a Random Forest Regressor from `sklearn.ensemble`
   * Enables a visualization of results in an interactive 3D surface plot, the ability to produce these interactive results with a minimal coding background, and four experimental presets to expound the designed use of functions
   * Compares the programmed hyperparamter optimization function to the public `GridSearchCV` from `sklearn.model_selection` in two areas: (1) speed of optimization program and (2) accuracy of optimization program
 
### V. Add More Predictors
 
   * Creates functions for imputation, encoding, pipeline, and cross-validation that are compatible with hyperparamter optimization and visualization functions derived in the above section
   * Extends graphing capabilities of previous functions to enable the juxtaposition of multiple datasets in an interactive 3D surface plot
 
### VI. XGB Regression

   * Extends the capabiility for the family of functions devised in Section IV to trivariate hyperparameter optimization and 4D graphical capabilites (color being the fourth dimension) to optimize and visualize how the number of trees ( `n_estimators` ), max depth of each tree ( `max_depth` ), and learning rate ( `learning_rate` ) influences model predictiveness
   * Maintains the bivariate hyperparameter optimization compatibility in the genus `experiment(...)` and `optimize(...)` developed in previous sections

## D. Exploring
To explore, tinker, and interact with all the functions, interactive surface plots, and optimization results, please follow these steps: 

| Steps | Visual | Rationale |
|-------|--------|-----------|
|1. For each section, there is a `README.md` file that covers the section's structure and highlights|  | *To offer more than perfunctory overview as described Section C. here*|
|2. To create coding playground with the function, simply click on the section's Jupyter notebook (the `.Ipynb` file), and then click the blue `Open to Colab` badge at the top| | *There are three reasons for opening to Colab: (1) this allows for data collected to be stored in one of line of code (and therefore quickly stored into a variable when needed) rather than splayed grotesquely in Github reader like this:  (2) Github blocks any javascript and thus the interactive surface plots do not render in Github, so viewing on Google Colab preserves the interactivity of the graphs, and (3) the file in Google Colab is distinct from the the uploaded copy, so one can tinker around with the code with a peace of mind.*|
|3. Open the table of contents| | *Navigate through the Jupyter Notebook with Google Colab's built-in table of contents*|
|4. **Important:** Make sure to run the `Initialization` tab in its entirety before exploring the section. This can easily be done by the method shown in the visual| | *Functions of each section build upon previous sections, and like a building without foundations, the section will fall apart with errors if certain fucntions are not defined* |
| 5. **Important:** Run the `Functions` and `Defining Predictors` tabs before exploring the subsections below it. | | *Certain sections use different predictors and this could affect a model's results and cause errors in the code* |
