# Machine Learning Portfolio
With the folllowing code, you can plot a 4D visualization of the hyperparameter optimization for a XGB Regressor Model:

    XGB_4D_e2 = experiment4D_with_XGB(200, range(2,7), range(1,101), X_train_pipeline, y, 
                                      preprocessor, NE_increment=30, cv = 1)
    A_data_4d_e2 = for_4D_plot_XGB(XGB_4D_e2)
    interactive_4Dsurface_XGB('Experiment 2', A_data_4d_e2)


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

Though we know roughly know what model's optimal parameters should look like, to find the most performant model we can call the `optimize(...)` function:

<p align="center">
  <img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20XGBR%20Optimized.gif"   width="500" /> 
</p>
<p align="center">
  <em>
    1st argument = data, 2nd argument = classifier (4D will have one more dimension than 3D)
  </em>
</p>


## I. About
The purpose of this portfolio is to (1) *evince* my ability to code machine learning (ML) models, (2) *showcase* my style of computative research, and most importantly, (3) to *politely shout out from the rooftops* my passion for machine learning. In this project, the Ames Housing Dataset, compiled in this [scientific paper](http://jse.amstat.org/v19n3/decock.pdf) by Dean De Cock, was used to build ML models that predict the sale price of houses. Both the training and testing datasets downloaded from Kaggle can be found in the `data` folder as `train_data.csv` and `test_data.csv`.

## II. Structure
The portfolio is broken up into the following structure:

1. Introduction (What you are reading now)
    
    * Crystalizes the main highlights of the portfolio and acts as a compass for a person navigating through the portoflio
  
2. Exploring the Data
    
    * 
    
3. Decision Tree Regression

    * Defines a family of functions for univariable hyperparameter optimization of the decision tree's max number of leaf nodes ( `max_leaf_nodes` ) in a Decision Tree Regressor from `sklearn.tree`
 
4. Random Forest Regression

    * Defines an family of functions for multivariable hyperparamter optimization of the number of trees ( `n_estimators` ) and max depth of each tree ( `max_depth` ) in a Random Forest Regressor from `sklearn.ensemble`
    * Enables a visualization of results in an interactive 3D surface plot, the ability to produce these interactive results with a minimal coding background, and four experimental presets expound claims
    * Compares the programmed hyperparamter optimization function to the public `GridSearchCV` from `sklearn.model_selection` in two areas: (1) speed of optimization program and (2) accuracy of optimization program
 
5. Add More Predictors
 
    * Creates functions for imputation, encoding, pipeline, and cross-validation that are compatible with hyperparamter optimization and visualization functions derived in the above section
    * Extends graphing capabilities of previous functions to enable the juxtaposition of multiple datasets in an interactive 3D surface plot
 
6. XGB Regression

    * Builds upon family of functions in Section IV in 4D (color being the fourth dimension) how the number of trees ( `n_estimators` ), max depth of each tree ( `max_depth` ), and learning rate ( `learning_rate` ) influences model predictiveness

## II. Exploring

## III. Highlights
