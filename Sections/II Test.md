# II. Taxonomy of Functions
## A. Family
### `experiment`
### `optimize`
### `initialize`
### `for_`
## B. Genus

## C. Species

## D. Ecosystems
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
