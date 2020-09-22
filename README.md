# About
*In this project, the Ames Housing Dataset, compiled in this [scientific paper](http://jse.amstat.org/v19n3/decock.pdf) by Dean De Cock was used to build ML models that predict the sale price of houses. The Mean Absolute Error (MAE) represents how close the model's sale price prediction was to the actual sale price. For instance, when* `MAE = 20000` *that signifies a model predicted housing sale prices on average within $20,000 of the actual housing sale prices.*

*Though many topics were discussed in the project, the main highlights were the trivariate hyperparameter optimization, 4D visualization of a XGBoost Regressor, capability to overlay multiple visualizations, and a taxonomical explanation of functions.*

## Highlights

<details><summary> "trivariate hyperparameter optimization" = Three variables of ML model were optimized to produce the lowest MAE </summary>

<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%202%20Abbreviated%20Magnified%20-%204D%20Surface%20Plot.gif"   width="500" /> 

</details>


<details><summary> "4D visualization" = Two variables + MAE were visualized in a 3D surface plot, and the third variable was visualized with color of the surface </summary>

| Without `zoom` function | With `zoom` function |
|-------------------------|----------------------|
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%203%20-%204D%20Surface%20Plot.gif"   width="500" />|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/Experiment%203%20Magnified%20-%204D%20Surface%20Plot.gif"   width="500" />| 

</details>


<details><summary> Capability to overlay multiple visualizations </summary>

| With `multicomparison` function |
|---------------------------------|
|<img src="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Animations/MultiPrefixAni.gif"   width="500" /> |

</details>



<details><summary> Taxonomical classification of functions (Refer to Section <a href="https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md">II Taxonomy of Functions</a>)   </summary>

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

</details>

## Structure 
*This portfolio is divided into six sections:*
### Machine Learning Makeshift Portfolio
  #### &emsp;&emsp; [I. Introduction](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/I%20Introduction.md)
  #### &emsp;&emsp; [II. Taxonomy of Functions](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/II%20Taxonomy%20of%20Functions.md)
  #### &emsp;&emsp; [III. Decision Tree Regressor](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/III%20Decision%20Tree%20Regressor.ipynb)
  #### &emsp;&emsp; [IV. Random Forest Regressor](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/IV%20Random%20Forest%20Regressor.ipynb)
  #### &emsp;&emsp; [V. Adding More Predictors](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/V%20Adding%20More%20Predictors.ipynb)
  #### &emsp;&emsp; [VI. XGBoost Regressor](https://github.com/rajtum/Machine-Learning-Makeshift-Portfolio/blob/master/Sections/VI%20XGBoost%20Regressor.ipynb)
  
# How to Explore
## Method 1)



## Method 2)
