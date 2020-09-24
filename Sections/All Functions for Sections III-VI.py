#Section III |
#------------

def train_model(model_arg, X_arg, y_arg):
  """
  Performs a train_test_split function to split the data into a training set and validation set.
  As the names suggest, inputted model trains on the training set, and then the function returns
  a list of the predictions for the validation y-values (target) and a list of the input validation
  x-values (predictors).

  train_model(my_model, predictors, target_variable)
  >>> returns my_model.predict(predictors), target_variable
  """
  train_X, val_X, train_y, val_y = train_test_split(X_arg, y_arg, random_state=1)

  model_arg.fit(train_X, train_y)
  return model_arg.predict(val_X), val_y

def test_model(model_arg, X_arg, y_arg, X_test_arg):
  """
  Same function as train_model except for the absence of a train_test_split function and no actual
  y-value output like val_y in train_model. Used to fit an optimized ML model with the entire
  predictors data before predicting with the test predictors dataset.
  """
  model_arg.fit(X_arg, y_arg)
  return model_arg.predict(X_test_arg)
def mae(model_arg, X_arg, y_arg):
  """
  Performs the same function as the mean_absolute_error with the addition of a
  model argument that incoporates the train_model function to return the
  mean absolute error (MAE). Note K-fold validation was added to later
  functions.

  mae(my_model, predictors, target_variable)
  >>> returns mean_absolute_error(pred_y, val_y)
  """
  pred_y, val_y = train_model(model_arg, X_arg, y_arg)
  mae = mean_absolute_error(pred_y, val_y)
  return mae

def initialize_DT(max_leaf_nodes_arg):
  """
  Creates a Decision Tree Regressor model with the specified max_leaf_nodes.

  initialize_DT(200)
  >>> DecisionTreeRegressor(max_leaf_nodes=200,random_state=1)
  """
  DT_model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes_arg, random_state=1)
  return DT_model

def experiment_with_DT(max_leaf_nodes_range_arg, X_arg, y_arg, is_data_table = False):
  """
  This model incorporates initialize_DT(), mae(), train_model() function to perform
  one of two actions: (1) a list of MAE values (if is_data_table = False or there is
  no specification) or (2) a dictionary with the keys as max_leaf_nodes (i.e. ints
  like 2,25,126) and values as the MAE values. Note that max_leaf_nodes_range_arg
  CANNOT be less than 2. The function finally returns the variable mae_results which
  is either intialized as a dictionary or list depending on teh is_data_table Boolean.

  experiment_with_DT(30, predictors, target, is_data_table = False)
  >>> returns mae_results = [MAE @ 2 max_leaf_nodes],...,[MAE @ 30 max_leaf_nodes]

  experiment_with_DT(30, predictors, target)
  >>> returns mae_results = [MAE @ 2 max_leaf_nodes],...,[MAE @ 30 max_leaf_nodes]

  experiment_with_DT(30, predictors, target, is_data_table = True)
  >>> returns mae_results = {2:MAE @ 2 max_leaf_nodes,...,30:MAE @ 30 max_leaf_nodes}
  """
  if is_data_table:
    mae_results = {}
  else:
    mae_results = []

  max_leaf_nodes_range = list(range(2,max_leaf_nodes_range_arg+1))
  
  for max_leaf_nodes in max_leaf_nodes_range:
    DT_model = initialize_DT(max_leaf_nodes)
    if is_data_table:
      mae_results[max_leaf_nodes] = mae(DT_model, X_arg, y_arg)
    else:
      mae_results.append(mae(DT_model, X_arg, y_arg))
  
  return mae_results

def optimize_DT(max_leaf_nodes_range_arg, X_arg, y_arg):
  """
  Further extends experiment_with_DT by finding the lowest mean absolute error 
  (best for the ML model) and then returns the corresponding max_leaf_node
  to the lowest MAE as a tuple such that (optimal max_leaf_node, lowest MAE).

  optimize_DT(200, predictors, target)
  >>> (71, 20123.142)
  """
  mae_results = experiment_with_DT(max_leaf_nodes_range_arg, X_arg, y_arg)
                                   
  min_mae = min(mae_results)
  optimal_leaf_node = mae_results.index(min_mae) + 2

  return (optimal_leaf_node, round(min_mae, 3))


### Abbreviated Functions
### ---------------------
### For information consult Section II on Taxonomy of Functions

def ewDT(max_leaf_nodes_range_arg, X_arg, y_arg, is_data_table = False):
  """
  Consult function experiment_with_DT for documentation.
  """
  return experiment_with_DT(max_leaf_nodes_range_arg, X_arg, y_arg, is_data_table = is_data_table)
def oDT(max_leaf_nodes_range_arg, X_arg, y_arg):
  """
  Consult function optimize_DT for documentation.
  """
  return optimize_DT(max_leaf_nodes_range_arg, X_arg, y_arg)
def iDT(max_leaf_nodes_arg):
  """
  Consult function optimize_DT for documentation.
  """
  return initialize_DT(max_leaf_nodes_arg)
  
#Section IV |
#-----------

def train_model(model_arg, X_arg, y_arg):
  """
  Performs a train_test_split function to split the data into a training set and validation set.
  As the names suggest, inputted model trains on the training set, and then the function returns
  a list of the predictions for the validation y-values (target) and a list of the input validation
  x-values (predictors).

  train_model(my_model, predictors, target_variable)
  >>> returns my_model.predict(predictors), target_variable
  """
  train_X, val_X, train_y, val_y = train_test_split(X_arg, y_arg, random_state=1)

  model_arg.fit(train_X, train_y)
  return model_arg.predict(val_X), val_y

def test_model(model_arg, X_arg, y_arg, X_test_arg):
  """
  Same function as train_model except for the absence of a train_test_split function and no actual
  y-value output like val_y in train_model. Used to fit an optimized ML model with the entire
  predictors data before predicting with the test predictors dataset.
  """
  model_arg.fit(X_arg, y_arg)
  return model_arg.predict(X_test_arg)

def mae(model_arg, X_arg, y_arg):
  """
  Performs the same function as the mean_absolute_error with the addition of a
  model argument that incoporates the train_model function to return the
  mean absolute error (MAE).

  mae(my_model, predictors, target_variable)
  >>> returns mean_absolute_error(pred_y, val_y)
  """
  pred_y, val_y = train_model(model_arg, X_arg, y_arg)
  mae = mean_absolute_error(pred_y, val_y)
  return mae

def initialize_Forest(n_estimators_arg, max_depth_arg, not_mae=False):
  """
  Creates a Random Forest Regressor model with the .

  initialize_DT(200)
  >>> DecisionTreeRegressor(max_leaf_nodes=200,random_state=1)
  """
  if not_mae:  
    Forest_model = RandomForestRegressor(n_estimators = n_estimators_arg,
                                         max_depth = max_depth_arg,
                                         random_state=1)
  else:
    Forest_model = RandomForestRegressor(n_estimators = n_estimators_arg,
                                         max_depth = max_depth_arg,
                                         criterion='mae',
                                         random_state=1)    
  return Forest_model

def experiment_with_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, is_data_table = False, NE_increment = 1, percent_complete = False):
  """
  Enables testing of Random Forest Model based on a n_estimators (number of trees) and max_depth(maximum depth of tree).
  
  TO SPEED UP FUNCTION:
  Change the increment of the n_estimators_range by defining NE_increment, if not defined, then defaults to 
  NE_increment = 1. The larger the increment, the less values in the range needed in computation.

  TO TRACK PROGRESS:
  Set percent_complete = True, if not percent_complete defaults to False. This is helpful for large ranges where you want
  to see progres of function. Note the increased time of running this feature has not been tested.

  TO INCREMENT:
  Consult "TO SPEED UP FUNCTION:" section for incrementing n_estimators_range. To change the increment of the max_depth_range 
  increment, simply change the argument from range(lower_bound, upper_bound) to range(lower_bound, upper_bound, range) like such:
  range(2,100, 5) increments by 5. For more information read up on range() documentation.

  OPTIMIZATION (FINDING THE LOWEST MAE VALUES):
  All output styles, whether processed as Data Table dictionary or simply an list of mae values, have the capability to be
  optimized. For output styles, consider (1) and (3) consider isDataTable_optimize_Forest and for (2) and (4) consider
  using the built-in optimization function optimize_Forest, which calls this method but simply outputs optimization
  results as a dictionary.

  OUTPUT STYLES:

  Four possible output styles: (1) and (3) meant for tables and figures, (2) and (4) meant for optimization.

  1) If max_depth_num_or_list_arg is an int and is_data_table is True, then function will return a dictionary with 
  max_depth_num and n_estimators stored in the key, and the mae stored as a key

  experiment_with_Forest(5, 10, X, y, is_data_table = True)
  >>> {'MD: 10, NT: 1': 29521.075342465752,
  >>>  'MD: 10, NT: 2': 27075.25,
  >>>  'MD: 10, NT: 3': 24907.708675799084,
  >>>  'MD: 10, NT: 4': 24415.24212328767,
  >>>  'MD: 10, NT: 5': 24446.186849315065}

  2) If max_depth_num_or_list_arg is an int but is_data_table is False, then function will return a list with mae
  values appended. Note that it is just a list of the values from dictionary produced in (1).

  experiment_with_Forest(5, 10, X, y, is_data_table = False)
  >>> [29521.075342465752,
  >>>  27075.25,
  >>>  24907.708675799084,
  >>>  24415.24212328767,
  >>>  24446.186849315065]

  *** Please refer to function optimize_Forest output style (1) for implementation of the above output style. ***
  
  3) If max_depth_num_or_list_arg is a list and is_data_table is True, then function will return a dictionary
  with the keys "MD: " max_depth (max_depth is an item within max_depth_range) and values in a 1 x 3 matrix
  [max_depth,mae_res,n_estimators] (n_estimators is an item within n_estimators_range). 

  experiment_with_Forest(5, range(1, 4), X, y, is_data_table = True)
  >>> {'MD: 1': [[1, 42865.78082191781, 1],
  >>>            [1, 42506.74520547945, 2],
  >>>            [1, 41979.210958904114, 3],
  >>>            [1, 41977.42465753425, 4],
  >>>            [1, 41950.30136986302, 5]],
  >>>  'MD: 2': [[2, 37515.40821917808, 1],
  >>>            [2, 37411.0301369863, 2],
  >>>            [2, 36447.74246575342, 3],
  >>>            [2, 35602.74246575342, 4],
  >>>            [2, 35679.468493150685, 5]],
  >>>  'MD: 3': [[3, 32610.49315068493, 1],
  >>>            [3, 32101.60821917808, 2],
  >>>            [3, 30171.314155251144, 3],
  >>>            [3, 28976.747260273973, 4],
  >>>            [3, 29039.537534246574, 5]]}

  *** Please refer to the function for_3D_plot_Forest for implementation of the above output style. ***

  4) If max_depth_num_or_list_arg is a list and is_data_table is False, then function will return a list with mae
  values appended (the same as (2) output style). Note that it is just a list of the second item in the list of
  values from dictionary produced in (3).

  experiment_with_Forest(5, range(1,4), X, y, is_data_table = False)
  >>> [42865.78082191781,
  >>>  42506.74520547945,
  >>>  41979.210958904114,
  >>>  41977.42465753425,
  >>>  41950.30136986302,
  >>>  37515.40821917808,
  >>>  37411.0301369863,
  >>>  36447.74246575342,
  >>>  35602.74246575342,
  >>>  35679.468493150685,
  >>>  32610.49315068493,
  >>>  32101.60821917808,
  >>>  30171.314155251144,
  >>>  28976.747260273973,
  >>>  29039.537534246574]

  """
  #Initializes whether function will return a dictionary or list
  if is_data_table:
    mae_results = {}
  else:
    mae_results = []

  #Creates a list from an the int arg n_estimators_range_arg starting at one and ending at the inputted int
  #If NE_increment is set to another number, then in increments the n_estimators range
  n_estimators_range = list(range(1, n_estimators_range_arg+1, NE_increment))

  #Checks to see what data type max_depth_num_or_list is
  if isinstance(max_depth_num_or_list_arg, int):
    max_depth_num = max_depth_num_or_list_arg
    #No need to run through max_depth numbers because there is only one
    for n_estimators in n_estimators_range:
      #Initializes model and calculuates MAE based on (X and y dataset,
      #NOT outputted x's and y's of n_estimators and mae)
      Forest_model = initialize_Forest(n_estimators, max_depth_num)
      mae_res = mae(Forest_model, X_arg, y_arg)
      #If true, adds a dictionary key (Max Depth) MD: max_depth_num, (Number of Trees) NT: n_estimators" to
      #gets the string "MD : max_depth_num, NT: n_estimators"
      if is_data_table:
        mae_results["MD: " + str(max_depth_num) + ", NT: " + str(n_estimators)] = mae_res
      #Else, adds the mae value calculated to a list (Best option for optimizating MAE at a certain max_depth_num)
      else:
        mae_results.append(mae_res)
      #Allows the progress of the function to be tracked in the console
      if percent_complete:
        print(str(round((n_estimators_range.index(n_estimators)+1)/len(n_estimators_range), 3)*100) +'%')
  #Since max_depth_num_or_list_arg is now a list, we need two for loops and we will recieve 3-dimensional data
  #3-dimensional because x = n_estimators, y = mae, z = max_depth
  #For visualization, consider [.......]
  else:
    max_depth_range = max_depth_num_or_list_arg
    if percent_complete:
      #Finds total number of iterations needed to complete function
      total_num_of_iterations = len(max_depth_range)*len(n_estimators_range)
    for max_depth in max_depth_range:
      #Now max_depth will be constant while it runs through all the n_estimators, then it will increase by 1 and iterate
      for n_estimators in n_estimators_range:
        #Intitializes model, calculates MAE with dataset, 
        #NOT outputted variables mentioned above (x = n_estimators...z = max_detph)
        Forest_model = initialize_Forest(n_estimators, max_depth)
        mae_res = mae(Forest_model, X_arg, y_arg)
        #If true, prepares data for becoming a 3-dimensional data set
        #Creates a dictionary with keys based on the max_depth, so
        #Calling one key will return all the mae values over n_estimators
        #at a certain max_depth, therefore making a 2-dimensional dataset
        #Since there are multiple 2-dimensional datasets, data can produce
        #a 3-dimensional plot
        if is_data_table:
          #Three variable matrix (x,y,z)
          mae_results.setdefault(max_depth, []).append([max_depth,mae_res,n_estimators])
        #Else, it returns an array (Best for mae optimization over max_depth_range and n_estimators)
        else:
          mae_results.append(mae_res)
        if percent_complete:
          #Finds the number of iterations completed by looking at indexes of n_estimators and max_depth
          num_of_iterations_completed = (n_estimators_range.index(n_estimators)+1) + (max_depth_range.index(max_depth)*len(n_estimators_range))
          num_of_iterations_completed_bef = (n_estimators_range.index(n_estimators)) + (max_depth_range.index(max_depth)*len(n_estimators_range))
          #Calculates percentage of function done, total_num_of_iterations defined at the beginning of else statement
          progress_percent = round((num_of_iterations_completed / total_num_of_iterations), 3) * 100
          progress_percent_bef = round((num_of_iterations_completed_bef / total_num_of_iterations), 3) * 100
          #Removes print if progress_precent hasn't changed
          if (progress_percent != progress_percent_bef):
            print(str(progress_percent) +'%')

  return mae_results

def optimize_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, NE_increment_arg = 1):
  """
  Optimizes a Random Forest Regressor based on a range of n_estimators and a range or
  specified max_depth. Note that to change the n_estimators_range_arg increment, you
  have to change NE_increment_arg NOT just NE_increment (note the arg at the end).
  
  Three possible input styles:

  1) If max_depth_num_or_list_arg is a num:
  
  optimze_Forest(5, 10, X, y)
  >>> {'max_depth': 10, 'Optimal MAE': 24415.24212328767, 'Optimal n_estimators': 4}

  2) If max_depth_num_or_list_arg is a list:

  optimze_Forest(5, range(1,4), X, y)
  >>> {'Optimal MAE': 28976.747260273973,
  >>>  'Optimal max_depth': 3,
  >>>  'Optimal n_estimators': 4}

  *** To validate these optimization results:

  experiment_with_Forest(5, range(1,4), X, y, is_data_table = True)
  >>> {'MD: 1': [[1, 42865.78082191781, 1],
  >>>           [1, 42506.74520547945, 2],
  >>>           [1, 41979.210958904114, 3],
  >>>           [1, 41977.42465753425, 4],
  >>>           [1, 41950.30136986302, 5]],
  >>>  'MD: 2': [[2, 37515.40821917808, 1],
  >>>           [2, 37411.0301369863, 2],
  >>>           [2, 36447.74246575342, 3],
  >>>           [2, 35602.74246575342, 4],
  >>>           [2, 35679.468493150685, 5]],
  >>>  'MD: 3': [[3, 32610.49315068493, 1],
  >>>           [3, 32101.60821917808, 2],
  >>>           [3, 30171.314155251144, 3],
  >>>           [3, 28976.747260273973, 4],  <------------ Lowest MAE value
  >>>           [3, 29039.537534246574, 5]]}

  3) If max_depth_num_or_list_arg is a list with increments > 1 and NE_increment_arg is > 1
     (i.e. any increment value, either for max_depth_range or n_estimators_range is > 1):

  optimze_Forest(5, range(1,6,2), X, y, NE_increment_arg = 2)
  >>> {'Optimal MAE': 25063.483013698627,
  >>>  'Optimal max_depth': 5,
  >>>  'Optimal n_estimators': 5}

  *** To validate these optimization results:

  experiment_with_Forest(5, range(1,6,2), X, y, NE_increment = 2, is_data_table=True)
  >>> {'MD: 1': [[1, 42865.78082191781, 1],
  >>>            [1, 41979.210958904114, 3],
  >>>            [1, 41950.30136986302, 5]],
  >>>  'MD: 3': [[3, 32610.49315068493, 1],
  >>>            [3, 30171.314155251144, 3],
  >>>            [3, 29039.537534246574, 5]],
  >>>  'MD: 5': [[5, 29782.660273972604, 1],
  >>>            [5, 25993.62511415525, 3],
  >>>            [5, 25063.483013698627, 5]]}  <----------- Lowest MAE value
  """
  #Checks to see if max_depth_num_or_list_arg is an int
  #experiment_with_Forest is_data_table naturally set to False
  if isinstance(max_depth_num_or_list_arg, int):
    max_depth_num = max_depth_num_or_list_arg
    #Tests Random Forest Regressor Model with given inputs and stores mae results in one-dimensional list
    mae_results = experiment_with_Forest(n_estimators_range_arg, max_depth_num, X_arg, y_arg, NE_increment=NE_increment_arg)
    #Finds the lowest MAE value in the list of mae_results
    min_mae = min(mae_results)
    #Locates the index of the lowest MAE value
    opt_n_estimators = (mae_results.index(min_mae)+1)*NE_increment_arg
    #Returns a dictionary wih optimized values, notes the max depth was not optimized here.
    return {'max_depth':max_depth_num, 'Optimal n_estimators':opt_n_estimators, 'Optimal MAE':min_mae}
  else:
    max_depth_range = max_depth_num_or_list_arg
    #Tests Random Forest Regressor Model with given inputs and stores mae results in one-dimensional list
    mae_results = experiment_with_Forest(n_estimators_range_arg, max_depth_range, X_arg, y_arg, NE_increment=NE_increment_arg)
    #Finds the loewst MAE value in the list of mae_results
    min_mae = min(mae_results)
    #Locates the index of the lowest MAE value
    min_mae_index = mae_results.index(min_mae)
    #Recreates n_estimators_range to locate the opt_n_estimators and opt_max_depth
    n_estimators_range = list(range(1,n_estimators_range_arg+1,NE_increment_arg))
    #Based on the min_mae_index, it finds the optimal max_depth and n_estimators
    opt_n_estimators = n_estimators_range[min_mae_index % len(n_estimators_range)]
    opt_max_depth = max_depth_range[min_mae_index // len(n_estimators_range)]
    #Returns a dictionary wih optimized values
    return {'Optimal max_depth':opt_max_depth, 'Optimal n_estimators':opt_n_estimators, 'Optimal MAE':min_mae}

def for_3D_plot_Forest(experiment_with_Forest_res):
  """
  Converts the dictionary returned in the (3) output style in function experiment_with_Forest to a 
  plottable 3D data via pyplot or plotly or some other structurally similar plotting modeule. Always
  refer to documentation on where (x,y,z) plot because in pyplot 'z' acts at the height variable of
  plot whereas plotly 'y' acts at the height variable plot.

  *** Numpy (as np) dependency ***
  max_depth_array, mae_array, n_estimators_array = for_3D_plot_Forest(experiment_with_Forest(5, range(1, 4), X, y, is_data_table = True))

  print('max_depth_array')
  print(max_depth_array)
  print('mae_array')
  print(mae_array)
  print('n_estimators_array')
  print(n_estimators_array)

  >>> max_depth_array
  >>> [[1. 2. 3.]
  >>> [1. 2. 3.]
  >>> [1. 2. 3.]
  >>> [1. 2. 3.]
  >>> [1. 2. 3.]]
  >>> mae_array
  >>> [[42865.78082192 37515.40821918 32610.49315068]
  >>> [42506.74520548 37411.03013699 32101.60821918]
  >>> [41979.2109589  36447.74246575 30171.31415525]
  >>> [41977.42465753 35602.74246575 28976.74726027]
  >>> [41950.30136986 35679.46849315 29039.53753425]]
  >>> n_estimators_array
  >>> [[1. 1. 1.]
  >>> [2. 2. 2.]
  >>> [3. 3. 3.]
  >>> [4. 4. 4.]
  >>> [5. 5. 5.]]
  """
  #Separates the keys from the values, remember all the needed data is in the values
  #Needed data = [max_depth,mae_res,n_estimators]
  (key_values, data_unzipped) = zip(*experiment_with_Forest_res.items())
  #Converted data_unzipped to an numpy array, where then data is sliced to max_depth
  #mae_res,n_estimators accordingly, transposed, and then stored accordingly
  data_array = np.array(data_unzipped)
  max_depth_vals = data_array[0:,0:,0].T
  mae_vals = data_array[0:,0:,1].T
  n_estimators_vals = data_array[0:,0:,2].T

  return max_depth_vals, mae_vals, n_estimators_vals

def zoom_3D_Forest(max_depth_arg, mae_arg, n_estimators_arg, mae_upper_limit):
  """
  Allows for the interactive_surface_Forest to focus on values below a certain mae_upper_limit to enhance
  granularity of interactive graph. The return variables are the same as for_3D_plot_Forest.
  """
  #Copies data, initializes important dictionaries
  A_data_arg = {'Max Depth of Each Tree':max_depth_arg, 'Number of Trees':n_estimators_arg, 'MAE':mae_arg}
  A_data = A_data_arg.copy()
  pruned_data = {}
  keys = {}
  for param in A_data_arg.keys():
    keys[param] = []

  #Filters for data rows based on if the 'mae' value is lower then mae_upper_limit
  A_data_test = A_data['MAE'] < mae_upper_limit
  for k in range(0, len(A_data_test)):
    #Clears shuttle_dict for next iteration
    shuttle_dict = {} 
    #Iterates through A_data_test at index k and appends parameters to shuttle_dict
    for i in range(0, len(A_data_test[k])):
      if A_data_test[k,i]:
        for param in keys.keys():
          shuttle_dict.setdefault(param, []).append(A_data[param][k,i])
    #Appends shuttle_values to pruned_data
    for param in shuttle_dict.keys():
      pruned_data.setdefault(param, []).append(shuttle_dict[param]) 
  return pruned_data['Max Depth of Each Tree'], pruned_data['MAE'], pruned_data['Number of Trees']

def plot_wireframe_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg):
  """
  Plots a wireframe with the desired formatting based on the data inputted.

  Dependencies
  *** matplotlib as mpl ***
  *** matplotlib.pyplot as plt ***
  """
  #Sets parameters for figure quality and text font (for consistency across notebook)
  mpl.rcParams['figure.dpi'] = 300
  plt.rcParams["font.family"] = "serif"

  #Additional step needed to change the labels and title
  sanserif = {'fontname':'serif'}

  #Sets size, defines 3d plot, sets all labels and title with desired font size and label padding, and viewing angle
  fig1=plt.figure(figsize=(20,15))
  ax = plt.axes(projection='3d')
  ax.plot_wireframe(max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg, color='black')
  ax.set_title(title + ' Wireframe Plot | Optimization of Random Forest Regression Model', fontdict = sanserif, fontsize=16, pad=60)
  ax.set_ylabel('Number of Trees', fontdict = sanserif, fontsize= 12, labelpad=10)
  ax.set_zlabel('Mean Absolute Error', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.set_xlabel('Max Depth of Each Tree', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.view_init(50, 35)

def pwFo(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg):
  """
  Consult plot_wireframe_Forest for documentation
  """
  return plot_wireframe_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)

def plot_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg):
  """
  Plots a surface plot with the desired formatting based on the data inputted.

  Dependencies
  *** matplotlib as mpl ***
  *** matplotlib.pyplot as plt ***
  """
  #Sets parameters for figure quality and text font (for consistency across notebook)
  mpl.rcParams['figure.dpi'] = 300
  plt.rcParams["font.family"] = "serif"

  #Additional step needed to change the labels and title
  sanserif = {'fontname':'serif'}

  #Sets size, defines 3d plot
  fig1=plt.figure(figsize=(20,15))
  ax = plt.axes(projection='3d')
  
  #Outlines the data with more structure before surfac plot
  ax.plot_wireframe(max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg, color='black')

  #Sets all labels and title with desired font size and label padding, and viewing angle
  ax.plot_surface(max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
  ax.set_title(title + ' Surface Plot | Optimization of Random Forest Regression Model', fontdict = sanserif, fontsize=16, pad=60)
  ax.set_ylabel('Number of Trees', fontdict = sanserif, fontsize= 12, labelpad=10)
  ax.set_zlabel('Mean Absolute Error', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.set_xlabel('Max Depth of Each Tree', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.view_init(50, 35)

def interactive_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg):
  """
  Creates an interactive surface plot with the desired formatting based on the data inputted.

  Dependencies
  *** plotly.graph_objects as go ***
  """
  #Creates surface figure based on data arguments
  fig = go.Figure(data=[go.Surface(z = mae_vals_arg, x = max_depth_vals_arg, y = n_estimators_vals_arg)])
  #Formats figure title, axis titles, dimesnions, and margins
  fig.update_layout(title= title + ' Interactive Surface Plot | Optimization of Random Forest Regression Model', autosize=True,
                    scene = dict(
                      xaxis_title='Max Depth of Each Tree',
                      yaxis_title='Number of Trees',
                      zaxis_title='Mean Absolute Error'),
                    width=1100, height=800,
                    margin=dict(l=65, r=50, b=65, t=90))
  fig.show()

def isDataTable_optimize_Forest(DataTable, n_estimators_range_arg, max_depth_num_or_list_arg, NE_increment_arg = 1):
  """
  Allows mae optimization for output styles (1) and (3) in the function experiment_with_Forest which output dictionaries.
  Returns the optimal max depth, optimal number of trees (n_estimators), and optimal mae in a dictionary.

  To optimize the mae value in your dictionary produced in experiment_with_Forest, simply copy over some key variables:

  experiment_2_Forest = experiment_with_Forest(100, range(2,101), X, y, is_data_table=True)

  Copy over the dictionary produced, n_estimators_range_arg (first arg) and max_depth_range_arg (second arg):

  isDataTable_optimize_Forest(experiment_2_Forest, 100, range(2,101))
  >>> {'Optimal MAE': 21705.35404109589,
  >>>  'Optimal max_depth': 26,
  >>>  'Optimal n_estimators': 58}
  """
  #Converts dictionary to list of mae values (mae_results)
  all_vals = np.array(list(DataTable.values()))
  only_mae_vals = all_vals[0:,0:,1].flatten()
  mae_results = list(only_mae_vals)

  #Same optimization coding used in the function optimize_Forest
  max_depth_range = max_depth_num_or_list_arg
  #Tests Random Forest Regressor Model with given inputs and stores mae results in one-dimensional lis
  #mae_results = experiment_with_Forest(n_estimators_range_arg, max_depth_range, X_arg, y_arg, NE_increment=NE_increment_arg)
  #Finds the loewst MAE value in the list of mae_results
  min_mae = min(mae_results)
  #Locates the index of the lowest MAE value
  min_mae_index = mae_results.index(min_mae)
  #Recreates n_estimators_range to locate the opt_n_estimators and opt_max_depth
  n_estimators_range = list(range(1,n_estimators_range_arg+1,NE_increment_arg))
  #Based on the min_mae_index, it finds the optimal max_depth and n_estimators
  opt_n_estimators = n_estimators_range[min_mae_index % len(n_estimators_range)]
  opt_max_depth = max_depth_range[min_mae_index // len(n_estimators_range)]
  #Returns a dictionary wih optimized values
  return {'Optimal max_depth':opt_max_depth, 'Optimal n_estimators':opt_n_estimators, 'Optimal MAE':min_mae}

def comparison_Grid_Search_Forest(n_estimators_arg, max_depth_arg, NE_increment = 1):
  """
  Performs a grid search based on an int n_estimators_arg and range max_depth_arg.
  Format is the same as the functions experiment_Forest and other related functions.

  comparison_Grid_Search_Forest(5, range(2,6))
  >>> {'Optimal MAE': 25181.08372830915,
  >>>  'Optimal max_depth': 5,
  >>>  'Optimal n_estimators': 5}
  """
  #Performs grid search according to the arguments given
  Grid_Search_Forest = GridSearchCV(estimator=RandomForestRegressor(),
                                    param_grid = {
                                        'n_estimators':range(1,n_estimators_arg+1, NE_increment),
                                        'max_depth': max_depth_arg,
                                    },
                                    scoring='neg_mean_absolute_error'
                                    )
  Grid_Search_Optimized_Forest = Grid_Search_Forest.fit(X, y)
  #Finds the optimal paramters and model
  opt_params = Grid_Search_Optimized_Forest.best_params_
  opt_Forest = Grid_Search_Optimized_Forest.best_estimator_
  #Stores data in a comparable format
  opt_data = {'Optimal MAE':mae(opt_Forest, X, y), 'Optimal max_depth':opt_params['max_depth'], 'Optimal n_estimators':opt_params['n_estimators']}
  return opt_data

def comparison_Forest(n_estimators_range_array_arg, max_depth_range_array_arg, NE_increment_targ = 1, MD_increment_targ = 1):
  """
  Compares the Grid Search optimization module in sklearn with the optimization program written for two characteristics:

  1) Execution Time (How long did it take for the function to complete?)
  Here it creates a dictionary of four different keys for four different methods of optimization, shown in time_results below, 
  and appends time to run each program in seconds to a list stored in each dictionary's values. To export to a dataframe,
  use the time_comparison_to_table function.

  2) MAE Optimization (What was the prediction accuracy of the function?)
  Creates a pandas Data Frame with the following columns:
  * Time Test: the nth iteration of testing the execution duration of the functions
  * Number of Trees Range: every POSSIBLE n_estimators parameter for plugged into the optimization function
                           to define the Random Forest Regressor Model (RFRM)
  * NE_increment: in the Number of Trees Range what n_estimators are ACTUALLY plugged into the optimization
                  function do define the RFRM. For instance, if NE_increment = 10 in a Number of Trees Range 
                  of 10-31, then the optimization function ran three iterations with RFRMs with the following
                  n_estimators = 10, then 20, and finally 30 because there was an increment of 10.
  * Max Depth of Tree Range: same principle as Number of Trees Range.
  * MD_increment: same principle as NE_increment. For instance, if MD_increment = 10 in a Max Depth of Tree
                  Range of 10-31, then the optimization function will ran three iterations with RFRMs of the
                  with following max_depth = 10, then 20, and finally 30 because ther was an increment of 10.
  * Type of Function: Specifies whether a row result was produced with the sklearn GridSearchCV module or the
                      programmed function.
  * Optimal MAE: What was the lowest MAE value in the list of MAE values? List of MAE values come from running 
                 the function over multiple ranges due to the Number of Trees Range, Max Depth of Tree Range,
                 NE_increment, MD_increment.
  * Optimal max_depth: What max_depth parameter produced the lowest MAE?
  * Optimal n_estimators: What n_estimators parameter produced the lowest MAE?

  *** GridSearchCV, pandas is a dependencey ***

  time_test, opt_test = time_comparison_Forest(range(10,21,10), range(10,21,10), NE_increment_targ=2, MD_increment_targ=2)
  
  (1) Execution Time
  print(time_test)
  >>> {'Created Data Table Optimization Times': [2.5442581176757812,
  >>>  24.136849641799927],
  >>>  'Grid Search Optimization Times': [2.2522621154785156, 19.751171588897705],
  >>>  'Preloaded Data Table Optimization Times': [5.3882598876953125e-05,
  >>>  0.00010013580322265625],
  >>>  'Programmed Optimization Times': [2.548872470855713, 24.11039972305298]}

  (2) MAE Optimization
  print(opt_test)
  * will print a DataFrame

  IMPORTANT INFO ABOUT ARGUMENTS:
  * Notice that inputting a range(10,21,10) in the first arg above (1) Results changes the n_estimators range evaluated in the function.
    It jumps from 1-10 to 1-20. If there was no range increment arg then it would returned a dictionar like this 1-10,  1-11... 1-19, 1-20.
    The 10 that dictates increments (third arg in range function) DOES NOT CHANGE THE NE_increment, it dictates the n_estimators range. 
    You have to change the NE_increment_targ (or n_estimators increment time argument) to change all of functions' increment at which it 
    evaluates MAE values.
  * In this time comparison function example, all the mae-calculating functions had an NE_increment of 2, meaning they calculated MAE values
    at n=1, n=3, n=5... and so one.
  * This same rule applies for the max_depth increment.
  * It is important you understand the distinction between the increment given in the range function and the variable argument increments.

  ABOUT DICTIONARY KEYS IN (1) Results:
  Created Data Table Optimization Times: when you run a experiment_with_Forest with is_data_table = True, and store the dictionary, which you
  optimize. (Contrast with preloaded, where it does NOT run experiment_with_Forest and goes straight to optimizing)

  Grid Search Optimization Times: time it takes for GridSearchCV to return optimized paramaters and mae values.
  
  Preloaded Data Table Optimization Times: Time it takes to optimize when experiment_with_Forest is already stored in a variable. (Contrast
  with Created Data Table Optimization Times)

  Programmed Optmization Times: time it takes for the function meant for optimization (i.e. optimize_Forest) to optimize model.
  """
  n_est_test = n_estimators_range_array_arg
  m_dep_test = max_depth_range_array_arg
  time_results = {'Grid Search Optimization': [], 'Programmed Optimization': [], 'Preloaded Data Table Optimization':[],
                  'Created Data Table Optimization': []}
  #Arguments must be the same length, refer to doc string for acceptable argument
  if len(n_estimators_range_array_arg) != len(max_depth_range_array_arg):
    print("ERROR: the list of first argument must be the same length as the list of second argument")
  #Runs and times Grid Search and Programed Function
  else:
    #Initializes empty lists to record all the key variables of the test
    time_test_list, n_est_range_list, m_dep_range_list, NE_incr_list, MD_incr_list  = [], [], [], [], []
    type_func_list, mae_res_list, n_est_opt_list, m_dep_opt_list = [],[],[],[]
    for i in range(0, len(n_estimators_range_array_arg)):
      #Records key variables into lists, duplicates because we will record for two functions
      for k in range(2):
        time_test_list.append(str(i+1))
        n_est_range_list.append('1-' + str(n_est_test[i]))
        m_dep_range_list.append('2-' + str(m_dep_test[i]+1))
        NE_incr_list.append(NE_increment_targ)
        MD_incr_list.append(MD_increment_targ)
      #Records start and end time of function and appends difference to respective key
      # GS - Gridsearch
      # r1, r2, r3 save results, but only r1 and r3 are added to dictionary because r2 will equal r3
      # r3 is added for timing consistency
      t0_GS = time.time()
      r1 = comparison_Grid_Search_Forest(n_est_test[i], range(2, m_dep_test[i]+1, MD_increment_targ), NE_increment = NE_increment_targ)
      t1_GS = time.time()
      time_results['Grid Search Optimization'].append([t1_GS - t0_GS, n_est_test[i], m_dep_test[i]])
      # PF = Programmed Function
      t0_PF = time.time()
      r2 = optimize_Forest(n_est_test[i], range(2, m_dep_test[i]+1, MD_increment_targ), X, y, NE_increment_arg = NE_increment_targ)
      t1_PF = time.time()
      time_results['Programmed Optimization'].append([t1_PF - t0_PF, n_est_test[i], m_dep_test[i]])
      # CDT = Created Data Table
      # PDT = Programmed Data Table
      # For the sake of controlling the environemnt to one line of code, the both functions args were not divided over two lines, which
      # would have improved readibility
      t0_CDT = time.time()
      data_table_temp = experiment_with_Forest(n_est_test[i], range(2, m_dep_test[i]+1, MD_increment_targ), X, y, is_data_table = True, NE_increment = NE_increment_targ)
      t0_PDT = time.time()
      r3 = isDataTable_optimize_Forest(data_table_temp, n_est_test[i], range(2, m_dep_test[i]+1, MD_increment_targ), NE_increment_arg = NE_increment_targ)
      t1_DT = time.time()
      time_results['Preloaded Data Table Optimization'].append([t1_DT - t0_PDT, n_est_test[i], m_dep_test[i]])
      time_results['Created Data Table Optimization'].append([t1_DT - t0_CDT, n_est_test[i], m_dep_test[i]])
      #Records the type of function used and mae optimization result
      type_func_list.append('Grid Search Optimization')
      mae_res_list.append(r1['Optimal MAE'])
      m_dep_opt_list.append(r1['Optimal max_depth'])
      n_est_opt_list.append(r1['Optimal n_estimators'])
      type_func_list.append('Programmed Optimization')
      mae_res_list.append(r3['Optimal MAE'])
      m_dep_opt_list.append(r3['Optimal max_depth'])
      n_est_opt_list.append(r3['Optimal n_estimators'])
    opt_dictionary = {'Time Test':time_test_list, 'Number of Trees Range':n_est_range_list, 'Max Depth of Tree Range':m_dep_range_list,
                   'NE_increment':NE_incr_list, 'MD_increment':MD_incr_list, 'Type of Function': type_func_list, 'Optimal MAE':mae_res_list,
                    'Optimal Max Depth':m_dep_opt_list,'Optimal Number of Trees':n_est_opt_list}
    optimization_results = pd.DataFrame(opt_dictionary)
  #optimization_results = optimization_results.reindex(list(opt_dictionary.keys()))
  return time_results, optimization_results

def time_comparison_to_table(time_comp_arg):
  """
  Converts the function comparison_Forest to plottable 2D table data.

  *** pandas is a dependency ***
  """
  time_comp_org = {}

  #Finds each execution duration and appends it to a temp array, which is then
  #added to the specific key, which is the type of function used,
  for element in time_comp_arg:
    temp_array = []
    for array in range(len(time_comp_arg[element])):
      temp_array.append(time_comp_arg[element][array][0])
    time_comp_org[element] = temp_array
  n_estimators_array = []
  max_depth_array = []
  #Adds the n_estimators and max_depth values to the dictionary
  for array in range(len(time_comp_arg['Created Data Table Optimization'])):
    n_estimators_array.append(time_comp_arg['Created Data Table Optimization'][array][1])
    max_depth_array.append(time_comp_arg['Created Data Table Optimization'][array][2])
  time_comp_org['Number of Trees'], time_comp_org['Max Depth of Each Tree'] = n_estimators_array, max_depth_array
  #Creates a DataFrame and then organizations the data in the desired format
  time_comp_table = pd.DataFrame(time_comp_org)
  columnsTitles = ['Number of Trees', 'Max Depth of Each Tree', 'Programmed Optimization', 'Grid Search Optimization', 
                   'Created Data Table Optimization', 'Preloaded Data Table Optimization']
  time_comp_table = time_comp_table.reindex(columns=columnsTitles)
  return time_comp_table
def time_comparison_plot(graph_title, x_axis_arg, time_comp_table_arg, custom_x_axis_title=''):
  """
  Creates a plotly line graph for the time comparison data based on the Data table produced
  from the function time_comparison_to_table. The time will always be the y-axis data value
  but the x-axis data is mutable via x_axis_arg in addition to the x-axis title.

  * x_axis_arg is a expected to be a string which is a column title for the time_comp_table_arg
    DataFrame

  *** plotly is a dependency ***
  """
  df = time_comp_table_arg
  fig = go.Figure()
  types_of_opt = ['Programmed Optimization', 'Grid Search Optimization', 'Created Data Table Optimization',
                 'Preloaded Data Table Optimization']
                 
  for opt_type in types_of_opt:
    fig.add_trace(go.Scatter(x=df[x_axis_arg], y=df[opt_type],
                             mode='lines+markers',
                             name=opt_type))
  if len(custom_x_axis_title) == 0:
    fig.update_layout(title= graph_title + ' | Optimization Time for Each Function Based on ' + x_axis_arg + ' Range',
                      xaxis_title=x_axis_arg,
                      yaxis_title='Time (sec)')
  else:
    fig.update_layout(title= graph_title + ' | Optimization Time for Each Function Based on ' + custom_x_axis_title + ' Range',
                      xaxis_title=custom_x_axis_title,
                      yaxis_title='Time (sec)')
  fig.show()
def opt_comparison_plot(graph_title, x_axis_arg, opt_comp_table_arg, custom_x_axis_title=''):
  """
  Creates a plotly line graph for the optimization comparison between the sklearn GridSearchCV
  function and the local function (the one programmed here). The lowest MAE value will always
  be the y-axis data value but the x-axis dat is mutable via x_axis_arg in addition to the
  x-axist title.

  * x_axis_arg is a expected to be a string which is a column title for the opt_comp_table_arg
    DataFrame
  *** plotly is a dependency ***
  """
  df = opt_comp_table_arg
  fig = px.line(df, x=x_axis_arg, y="Optimal MAE", color='Type of Function',
              hover_data=['Type of Function']).for_each_trace(lambda t: t.update(name=t.name.split("=")[1]))

  if len(custom_x_axis_title) == 0:
    fig.update_layout(title= graph_title + ' | Optimal MAE from Each Function Based on ' + x_axis_arg,
                      xaxis_title=x_axis_arg,
                      yaxis_title='Optimal MAE')
  else:
    fig.update_layout(title= graph_title + ' | Optimal MAE from Each Function Based on ' + custom_x_axis_title,
                  xaxis_title=custom_x_axis_title,
                  yaxis_title='Optimal MAE')
  fig.show()

### Abbreviated Functions
### ---------------------
### For information consult Section II on Taxonomy of Functions
def ewFo(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, is_data_table = False, NE_increment = 1, percent_complete = False):
  """
  Consult with experiment_with_Forest for documentation.
  """
  return experiment_with_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, is_data_table = is_data_table, NE_increment = NE_increment, percent_complete = percent_complete)
def oFo(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, NE_increment_arg = 1):
  """
  Consult optimize_Forest for documentation.
  """
  return optimize_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, NE_increment_arg = NE_increment_arg)
def f3DpFo(experiment_with_Forest_res):
  """
  Consult for_3D_plot_Forest for documentation.
  """
  return for_3D_plot_Forest(experiment_with_Forest_res)
def z3Fo(max_depth_arg, mae_arg, n_estimators_arg, mae_upper_limit):
  """
  Consult zoom_3D_Forest for documentation.
  """
  return zoom_3D_Forest(max_depth_arg, mae_arg, n_estimators_arg, mae_upper_limit)
def psFo(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg):
  """
  Consult plot_surface_Forest for documentation.
  """
  return plot_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)
def isFo(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg):
  """
  Consult interactive_surface_Forest for documentation.
  """
  return interactive_surface_Forest(title, max_depth_vals_arg, n_estimators_vals_arg, mae_vals_arg)
def i_oFo(DataTable, n_estimators_range_arg, max_depth_num_or_list_arg, NE_increment_arg = 1):
  """
  Consult isDataTable_optimize_Forest for documentation.
  """
  return isDataTable_optimize_Forest(DataTable, n_estimators_range_arg, max_depth_num_or_list_arg, NE_increment_arg = NE_increment_arg)
def cGFo(n_estimators_arg, max_depth_arg, NE_increment = 1):
  """
  Consult comparison_Grid_Search_Forest for documentation.
  """
  return comparison_Grid_Search_Forest(n_estimators_arg, max_depth_arg, NE_increment = NE_increment)
def cFo(n_estimators_range_array_arg, max_depth_range_array_arg, NE_increment_targ = 1, MD_increment_targ = 1):
  """
  Consult comparison_Forest for documentation.
  """
  return comparison_Forest(n_estimators_range_array_arg, max_depth_range_array_arg, NE_increment_targ = NE_increment_targ, MD_increment_targ = NE_increment_targ)
def t_cto(time_comp_arg):
  """
  Consult time_comparison_to_table for documentation.
  """
  return time_comparison_to_table(time_comp_arg)
def t_cpl(graph_title, x_axis_arg, time_comp_table_arg, custom_x_axis_title=''):
  """
  Consult time_comparison_plot for documentation.
  """
  return time_comparison_plot(graph_title, x_axis_arg, time_comp_table_arg, custom_x_axis_title=custom_x_axis_title)
def o_cpl(graph_title, x_axis_arg, opt_comp_table_arg, custom_x_axis_title=''):
  """
  Consult opt_comparison_plot for documentation.
  """
  return opt_comparison_plot(graph_title, x_axis_arg, opt_comp_table_arg, custom_x_axis_title=custom_x_axis_title)
def iFo(n_estimators_arg, max_depth_arg, not_mae=False):
  """
  Consult initialize_Forest for documentation.
  """
  return initialize_Forest(n_estimators_arg, max_depth_arg, not_mae=not_mae)

#Section V |
#----------

#Section V.A

def impute(X_arg, drop_thresh = 2/3):
  """
  Isolates the numerical data columns and then drops any column that does not have the
  drop_thresh amount of data entries. At default, this is set to 2/3 meaning that if a
  column does not have at least 2/3 of the rows filled with data, then it drops the 
  column. After imputing the remaining columns that meet the drop_thresh but are still
  missing values, the funciton returns the DataFrame imputed_X
  """
  #Filters for only numerical columns
  X_arg_nums = X_arg.select_dtypes(exclude = ['object'])
  #Finds columns with any missing values
  missing_val_columns = [col for col in X_arg_nums.columns if X_arg_nums[col].isnull().any()]
  #Calculates the amount of rows needed to have data for the column not to be dropped
  drop_thresh_amount = drop_thresh * len(X_arg_nums.index)
  #Drops any columns that do not have a minimum amount of data, set at least 2/3
  #Removes those columns from list imputable_columns, which will be imputed
  imputable_columns = missing_val_columns
  for col in missing_val_columns:
    if X_arg_nums[col].isnull().sum() >= drop_thresh_amount:
      X_arg_nums.drop(col, axis = 0, inplace = True)
      imputable_columns.remove(col)
  #Imputes the colums with enough data
  imputer = SimpleImputer()
  imputed_X = pd.DataFrame(imputer.fit_transform(X_arg_nums))
  #Returns columns to imputed DataFrame
  imputed_X.columns = X_arg_nums.columns
  return imputed_X
def comparison_plot_surface_Forest(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                   A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0):
  """
  Plots two surface plots with the desired formatting based on the data inputted. Arguments with
  a letter_alpha control transparency of juxtaposed graphs, letter_label create interactive annotations
  to help to distinguish between groups of data, and letter_label_sep offers limited control over
  separating labels that materialize to close to one another.

  Dependencies
  *** matplotlib as mpl ***
  *** matplotlib.pyplot as plt ***
  """
  #Sets parameters for figure quality and text font (for consistency across notebook)
  mpl.rcParams['figure.dpi'] = 300
  plt.rcParams["font.family"] = "serif"

  #Additional step needed to change the labels and title
  sanserif = {'fontname':'serif'}

  #Sets size, defines 3d plot
  fig1=plt.figure(figsize=(20,15))
  ax = plt.axes(projection='3d')
  
  #Plots all the 3D data to a surface plot
  #Sets all labels and title with desired font size and label padding, and viewing angle
  ax.plot_surface(A_data['Max Depth'], A_data['Number of Trees'], A_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =a_alpha, antialiased=True)
  ax.plot_surface(B_data['Max Depth'], B_data['Number of Trees'], B_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =b_alpha, antialiased=True)
  ax.set_title(title + ' Surface Plot | Optimization of Random Forest Regression Model', fontdict = sanserif, fontsize=16, pad=60)
  ax.set_ylabel('Number of Trees', fontdict = sanserif, fontsize= 12, labelpad=10)
  ax.set_zlabel('Mean Absolute Error', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.set_xlabel('Max Depth of Each Tree', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.text(min(A_data['Max Depth'].flatten()) - min(A_data['Max Depth'].flatten())*.01, 
          max(A_data['Number of Trees'].flatten()), 
          min(A_data['MAE'].flatten()) + min(A_data['MAE'].flatten()) *.005 + a_label_sep,
          A_label, fontsize = 12, style='italic')
  ax.text(min(B_data['Max Depth'].flatten()) - min(B_data['Max Depth'].flatten())*.01, 
          max(B_data['Number of Trees'].flatten()), 
          min(B_data['MAE'].flatten()) + min(B_data['MAE'].flatten()) *.005 + b_label_sep,
          B_label, fontsize = 12, style='italic')  
  ax.view_init(50, 35)
def comparison_interactive_surface_Forest(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                          A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0):
  """
  Creates two interactive surface plots with the desired formatting based on the data inputted. Arguments with
  a letter_alpha control transparency of juxtaposed graphs, letter_label create interactive annotations
  to help to distinguish between groups of data, and letter_label_sep offers limited control over
  separating labels that materialize to close to one another.

  Dependencies
  *** plotly.graph_objects as go ***
  """
  #Creates surface figure based on data arguments
  fig = go.Figure(data=[go.Surface(z = A_data['MAE'], x = A_data['Max Depth'], y = A_data['Number of Trees'], 
                                   opacity=a_alpha),
                        go.Surface(z = B_data['MAE'], x = B_data['Max Depth'], y = B_data['Number of Trees'], 
                                   opacity=b_alpha, showscale=False)])
  #Formats figure title, axis titles, dimesnions, and margins
  fig.update_layout(title= title + ' Interactive Surface Plot | Optimization of Random Forest Regression Model', autosize=True,
                    scene = dict(xaxis_title='Max Depth of Each Tree',
                                 yaxis_title='Number of Trees',
                                 zaxis_title='Mean Absolute Error',
                                 annotations= [dict(showarrow=False,
                                                    x=min(A_data['Max Depth'].flatten()),
                                                    y=max(A_data['Number of Trees'].flatten()),
                                                    z=min(A_data['MAE'].flatten()),
                                                    text=A_label,
                                                    xanchor="left",
                                                    xshift=min(A_data['Max Depth'].flatten())*.05,
                                                    yshift=min(A_data['MAE'].flatten())*.001 + a_label_sep/100,
                                                    opacity=0.7
                                              ),
                                              dict(showarrow=False,
                                                   x=min(B_data['Max Depth'].flatten()),
                                                   y=max(B_data['Number of Trees'].flatten()),
                                                   z=min(B_data['MAE'].flatten()),
                                                   text=B_label,
                                                   xanchor="left",
                                                   xshift=min(B_data['Max Depth'].flatten())*.05,
                                                   yshift=min(B_data['MAE'].flatten())*.001 + b_label_sep/100,
                                                   opacity=0.7
                                              )]
                                 ),
                    width=1100, height=800,
                    margin=dict(l=65, r=50, b=65, t=90),
                    )
  fig.show()
def for_3D_comp_Forest(max_depth_arg, mae_arg, n_estimators_arg):
  """
  Formats the data returned in the function for_3D_plot_Forest into a dictionary that simplifies
  the arguments for the comparison graph functions.
  """
  A_data = {'Max Depth': max_depth_arg, 'MAE':mae_arg, 'Number of Trees':n_estimators_arg}
  return A_data

### Abbreviated Functions
### ---------------------
### For information consult Section II on Taxonomy of Functions
def f3DcFo(max_depth_arg, mae_arg, n_estimators_arg):
  """
  Consult for_3D_comp_Forest for documentation.
  """
  return for_3D_comp_Forest(max_depth_arg, mae_arg, n_estimators_arg)

def cpFo(title, A_data, B_data, a_alpha = .8, b_alpha = .8, A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0):
  """
  Consult comparison_plot_surface_Forest for documentation.
  """
  return comparison_plot_surface_Forest(title, A_data, B_data, a_alpha = a_alpha, b_alpha = b_alpha, A_label = A_label, 
                                        B_label = B_label, a_label_sep = a_label_sep, b_label_sep = b_label_sep)
def ciFo(title, A_data, B_data, a_alpha = .8, b_alpha = .8, A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0):
  """
  Consult comparison_plot_surface_Forest for documentation.
  """
  return comparison_interactive_surface_Forest(title, A_data, B_data, a_alpha = a_alpha, b_alpha = b_alpha, A_label = A_label, 
                                        B_label = B_label, a_label_sep = a_label_sep, b_label_sep = b_label_sep)

#Section V.B

def encode(X_train_arg, X_test_arg, cardinality_thresh = 10):
  """
  Performs label encoding on any columns with a cardinality above the cardinality_thresh and
  one-hot encoding for the remaining columns.
  """
  #Remove any columns without data values (do not worry about numbers, we have impute() to consider that dtype)
  cols_missing_train = [col for col in X_train_arg.columns if X_train_arg[col].isnull().any()]
  cols_missing_test = [col for col in X_test_arg.columns if X_test_arg[col].isnull().any()]
  X_train = X_train_arg.drop(cols_missing_train, axis = 1)
  X_train.drop(cols_missing_test, axis = 1, inplace = True)
  X_test = X_test_arg.drop(cols_missing_train, axis = 1)
  X_test.drop(cols_missing_test, axis = 1, inplace = True)
  #Finding all the categorical data columns, one-hot encoding columns, and potential label encoding columns
  category_columns = [col for col in X_train.columns if X_train[col].dtype == 'object']
  one_hot_columns = [col for col in category_columns if X_train[col].nunique() <= cardinality_thresh]
  potential_label_columns = list(set(category_columns) - set(one_hot_columns))
  #Finds label columns by making sure all the unique values in the X_train are in the X_test
  label_columns = []
  #Runs through all the potential label columns
  for col in potential_label_columns:
    #Finds all the unique values in either training or testing dataset within the column
    unique_vals_train = set(X_train[col])
    unique_vals_test = set(X_test[col])
    #If the the set of unique values equals each other, than label encoding will work, append
    if unique_vals_train == unique_vals_test:
      label_columns.append(col)
    #If the length of the unique values in training set is larger than testing set, lets look to see if
    #all the unique values in the testing set are also found in the training set (meaning the training set
    #has a few extra unique values) If true, append
    elif len(unique_vals_train) > len(unique_vals_test):
      if unique_vals_test.intersection(unique_vals_train) == unique_vals_test:
        label_columns.append(col)
  #Create one-hot encoder and encode training and testing datasets
  OH_encoder = OneHotEncoder(handle_unknown = 'ignore', sparse = False)
  OH_X_train = pd.DataFrame(OH_encoder.fit_transform(X_train_arg[one_hot_columns]))
  OH_X_test = pd.DataFrame(OH_encoder.transform(X_test_arg[one_hot_columns]))
  #Return indices to one-hot encoder result
  OH_X_train.index = X_train_arg.index
  OH_X_test.index = X_test_arg.index
  #Create label encoder and encode training and testing datasets
  label_encoder = LabelEncoder()
  for col in label_columns:
    label_X_train = pd.DataFrame({col:label_encoder.fit_transform(X_train_arg[col])})
    label_X_test = pd.DataFrame({col:label_encoder.transform(X_test_arg[col])})
  label_X_train.index = X_train_arg.index
  label_X_test.index = X_test_arg.index
  #Now, we have done all the encoding, time to concatenate DataFrames
  encoded_X_train = pd.concat([OH_X_train, label_X_train], axis = 1)
  encoded_X_test = pd.concat([OH_X_test, label_X_test], axis = 1)
  return encoded_X_train, encoded_X_test
def multicomparison_plot_surface_Forest(title, A_data, B_data, C_data, 
                                        a_alpha = .8, b_alpha = .8, c_alpha = .8,
                                        A_label = '', B_label = '', C_label = '',
                                        a_label_sep = 0, b_label_sep = 0, c_label_sep = 0,
                                        D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0,
                                        E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0):
  """
  Allows multiple surface plots (5 Max) with the desired formatting based on the data inputted.
  Check the sister method comparison_plot_surface_Forest for comparisons with only two datsets.
  Note that here dictionaries will be the arguments rather than the values of the dictionaries'
  being directly entered, so data returned from a for_plot can be plotted with a single arguemnt.
  Arguments with a letter_alpha control transparency of juxtaposed graphs, letter_label create 
  interactive annotations to help to distinguish between groups of data, and letter_label_sep 
  offers limited control over separating labels that materialize to close to one another.

  Dependencies
  *** matplotlib as mpl ***
  *** matplotlib.pyplot as plt ***
  """
  #Sets parameters for figure quality and text font (for consistency across notebook)
  mpl.rcParams['figure.dpi'] = 300
  plt.rcParams["font.family"] = "serif"

  #Additional step needed to change the labels and title
  sanserif = {'fontname':'serif'}

  #Sets size, defines 3d plot
  fig1=plt.figure(figsize=(20,15))
  ax = plt.axes(projection='3d')
  
  #Plots all the 3D data to a surface plot
  #Sets all labels and title with desired font size and label padding, and viewing angle
  ax.plot_surface(A_data['Max Depth'], A_data['Number of Trees'], A_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =a_alpha, antialiased=True)
  ax.plot_surface(B_data['Max Depth'], B_data['Number of Trees'], B_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =b_alpha, antialiased=True)
  ax.plot_surface(C_data['Max Depth'], C_data['Number of Trees'], C_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =c_alpha, antialiased=True)
  #Checks to see if there is any data in D_data or E_data, and plots a surface if there is
  if D_data != {}:
    ax.plot_surface(D_data['Max Depth'], D_data['Number of Trees'], D_data['MAE'], rstride=1, cstride=1, 
                    cmap='viridis', edgecolor='none', alpha =d_alpha, antialiased=True)
    ax.text(min(D_data['Max Depth'].flatten()) - min(D_data['Max Depth'].flatten())*.01, 
            max(D_data['Number of Trees'].flatten()), 
            min(D_data['MAE'].flatten()) + min(D_data['MAE'].flatten()) *.005 + d_label_sep,
            D_label, fontsize = 12, style='italic')
  if E_data != {}:
    ax.plot_surface(E_data['Max Depth'], E_data['Number of Trees'], E_data['MAE'], rstride=1, cstride=1, 
                    cmap='viridis', edgecolor='none', alpha =e_alpha, antialiased=True)
    ax.text(min(E_data['Max Depth'].flatten()) - min(E_data['Max Depth'].flatten())*.01, 
            max(E_data['Number of Trees'].flatten()), 
            min(E_data['MAE'].flatten()) + min(E_data['MAE'].flatten()) *.005 + e_label_sep,
            E_label, fontsize = 12, style='italic')
  #Organizes all the formatting, such as the plot title, axis titles, plot annotations
  ax.set_title(title + ' Surface Plot | Optimization of Random Forest Regression Model', fontdict = sanserif, fontsize=16, pad=60)
  ax.set_ylabel('Number of Trees', fontdict = sanserif, fontsize= 12, labelpad=10)
  ax.set_zlabel('Mean Absolute Error', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.set_xlabel('Max Depth of Each Tree', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.text(min(A_data['Max Depth'].flatten()) - min(A_data['Max Depth'].flatten())*.01, 
          max(A_data['Number of Trees'].flatten()), 
          min(A_data['MAE'].flatten()) + min(A_data['MAE'].flatten()) *.005 + a_label_sep,
          A_label, fontsize = 12, style='italic')
  ax.text(min(B_data['Max Depth'].flatten()) - min(B_data['Max Depth'].flatten())*.01, 
          max(B_data['Number of Trees'].flatten()), 
          min(B_data['MAE'].flatten()) + min(B_data['MAE'].flatten()) *.005 + b_label_sep,
          B_label, fontsize = 12, style='italic')  
  ax.text(min(C_data['Max Depth'].flatten()) - min(C_data['Max Depth'].flatten())*.01, 
          max(C_data['Number of Trees'].flatten()), 
          min(C_data['MAE'].flatten()) + min(C_data['MAE'].flatten()) *.005 + c_label_sep,
          C_label, fontsize = 12, style='italic')  
  ax.view_init(50, 35)
def multicomparison_interactive_surface_Forest(title, A_data, B_data, C_data, 
                                               a_alpha = .8, b_alpha = .8, c_alpha = .8,
                                               A_label = '', B_label = '', C_label = '',
                                               a_label_sep = 0, b_label_sep = 0, c_label_sep = 0,
                                               D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0,
                                               E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0):
  """
  Allows multiple intereactive surface plots (5 Max) with the desired formatting based on the data inputted.
  Check the sister method comparison_interactive_surface_Forest for comparisons with only two datsets.
  Note that here dictionaries will be the arguments rather than the values of the dictionaries'
  being directly entered, so data returned from a for_plot can be plotted with a single arguemnt.
  Arguments with a letter_alpha control transparency of juxtaposed graphs, letter_label create 
  interactive annotations to help to distinguish between groups of data, and letter_label_sep 
  offers limited control over separating labels that materialize to close to one another.

  Dependencies
  *** plotly.graph_objects as go ***
  """
  #Creates surface figure based on data arguments
  fig = go.Figure(data=[go.Surface(z = A_data['MAE'], x = A_data['Max Depth'], y = A_data['Number of Trees'], 
                                   opacity=a_alpha),
                        go.Surface(z = B_data['MAE'], x = B_data['Max Depth'], y = B_data['Number of Trees'], 
                                   opacity=b_alpha, showscale=False),
                        go.Surface(z = C_data['MAE'], x = C_data['Max Depth'], y = C_data['Number of Trees'], 
                                   opacity=c_alpha, showscale=False)
                        ])
  #Creates dynamic data labels that will be added with update_layout
  data_labels = [dict(showarrow=False,
                      x=min(A_data['Max Depth'].flatten()),
                      y=max(A_data['Number of Trees'].flatten()),
                      z=min(A_data['MAE'].flatten()),
                      text=A_label,
                      xanchor="left",
                      xshift=min(A_data['Max Depth'].flatten())*.05,
                      yshift=min(A_data['MAE'].flatten())*.001 + a_label_sep/100,
                      opacity=0.7),
                 dict(showarrow=False,
                      x=min(B_data['Max Depth'].flatten()),
                      y=max(B_data['Number of Trees'].flatten()),
                      z=min(B_data['MAE'].flatten()),
                      text=B_label,
                      xanchor="left",
                      xshift=min(B_data['Max Depth'].flatten())*.05,
                      yshift=min(B_data['MAE'].flatten())*.001 + b_label_sep/100,
                      opacity=0.7),
                 dict(showarrow=False,
                      x=min(C_data['Max Depth'].flatten()),
                      y=max(C_data['Number of Trees'].flatten()),
                      z=min(C_data['MAE'].flatten()),
                      text=C_label,
                      xanchor="left",
                      xshift=min(C_data['Max Depth'].flatten())*.05,
                      yshift=min(C_data['MAE'].flatten())*.001 + c_label_sep/100,
                      opacity=0.7)
                ]
  #Checks to see if there is anymore datasets, and adds those datasets
  if D_data != {}:
      fig.add_trace(go.Surface(z = D_data['MAE'], x = D_data['Max Depth'], y = D_data['Number of Trees'], 
                               opacity=d_alpha, showscale=False))
      data_labels.append(dict(showarrow=False,
                              x=min(D_data['Max Depth'].flatten()),
                              y=max(D_data['Number of Trees'].flatten()),
                              z=min(D_data['MAE'].flatten()),
                                text=D_label,
                              xanchor="left",
                              xshift=min(D_data['Max Depth'].flatten())*.05,
                              yshift=min(D_data['MAE'].flatten())*.001 + d_label_sep/100,
                              opacity=0.7
                          ))
  if E_data != {}:
      fig.add_trace(go.Surface(z = E_data['MAE'], x = E_data['Max Depth'], y = E_data['Number of Trees'], 
                               opacity=e_alpha, showscale=False))
      data_labels.append(dict(showarrow=False,
                              x=min(E_data['Max Depth'].flatten()),
                              y=max(E_data['Number of Trees'].flatten()),
                              z=min(E_data['MAE'].flatten()),
                                text=E_label,
                              xanchor="left",
                              xshift=min(E_data['Max Depth'].flatten())*.05,
                              yshift=min(E_data['MAE'].flatten())*.001 + e_label_sep/100,
                              opacity=0.7
                          ))                        
  #Formats figure title, axis titles, dimesnions, and margins
  fig.update_layout(title= title + ' Interactive Surface Plot | Optimization of Random Forest Regression Model', autosize=True,
                      scene = dict(xaxis_title='Max Depth of Each Tree',
                                  yaxis_title='Number of Trees',
                                  zaxis_title='Mean Absolute Error',
                                  annotations= data_labels
                                  ),
                      width=1100, height=800,
                      margin=dict(l=65, r=50, b=65, t=90),
                   )
  fig.show()

### Abbreviated Functions
### ---------------------
### For information consult Section II on Taxonomy of Functions
def m_cpFo(title, A_data, B_data, C_data, a_alpha = .8, b_alpha = .8, c_alpha = .8, 
           A_label = '', B_label = '', C_label = '', a_label_sep = 0, b_label_sep = 0, 
           c_label_sep = 0, D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0, 
           E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0):
  """
  Consult multicomparison_plot_surface_Forest for documentation.
  """
  return multicomparison_plot_surface_Forest(title, A_data, B_data, C_data, a_alpha = a_alpha, b_alpha = b_alpha, c_alpha = c_alpha, 
                                             A_label = A_label, B_label = B_label, C_label = C_label, a_label_sep = a_label_sep, b_label_sep = b_label_sep, 
                                             c_label_sep = c_label_sep, D_data = D_data, d_alpha = d_alpha, D_label = D_label, d_label_sep = d_label_sep, 
                                             E_data = E_data, e_alpha = e_alpha, E_label = E_label, e_label_sep = e_label_sep)
def m_ciFo(title, A_data, B_data, C_data, a_alpha = .8, b_alpha = .8, c_alpha = .8, 
           A_label = '', B_label = '', C_label = '', a_label_sep = 0, b_label_sep = 0, 
           c_label_sep = 0, D_data = {}, d_alpha = .8, D_label = '', d_label_sep = 0, 
           E_data = {}, e_alpha = .8, E_label = '', e_label_sep = 0):
  """
  Consult multicomparison_plot_surface_Forest for documentation.
  """
  return multicomparison_interactive_surface_Forest(title, A_data, B_data, C_data, a_alpha = a_alpha, b_alpha = b_alpha, c_alpha = c_alpha, 
                                                    A_label = A_label, B_label = B_label, C_label = C_label, a_label_sep = a_label_sep, b_label_sep = b_label_sep, 
                                                    c_label_sep = c_label_sep, D_data = D_data, d_alpha = d_alpha, D_label = D_label, d_label_sep = d_label_sep, 
                                                    E_data = E_data, e_alpha = e_alpha, E_label = E_label, e_label_sep = e_label_sep)

# Section V.C

def mae(model_arg, X_arg, y_arg):
  """
  Performs the same function as the mean_absolute_error with the addition of a
  model argument that incoporates the train_model function to return the
  mean absolute error (MAE). Note K-fold validation was added to later
  functions.

  mae(my_model, predictors, target_variable)
  >>> returns mean_absolute_error(pred_y, val_y)
  """
  pred_y, val_y = train_model(model_arg, X_arg, y_arg)
  mae = mean_absolute_error(pred_y, val_y)
  return mae

def mae_cross_val(model_arg, X_arg, y_arg, cv_arg = 5):
  """
  Performs the same function as the cross_val_score, and then returns the mean of the K_fold validation with
  cv_arg folds, which defaults to 5 if none is specified, as a postive floating point. The standard deviation
  of all the folds is also returned.

  *** numpy as np is a dependency ***
  *** cross_val_score from sklearn.model_selection is dependency ***
  """
  mae_result_array = abs(cross_val_score(model_arg, X_arg, y_arg, scoring = 'neg_mean_absolute_error', cv = cv_arg))
  mae_result_mean = mae_result_array.mean()
  mae_result_sd = np.std(mae_result_array)
  return mae_result_mean, mae_result_sd
def initialize_Pipeline(preprocessor_arg, model_arg):
  """
  Initializes a Pipeline with given preprocessing method and ML model.
  """
  pipeline = Pipeline(steps=[('preprocessor', preprocessor_arg),
                             ('model', model_arg)])
  return pipeline
def experiment_with_pipelineCV_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, preprocessor_arg,
                                      NE_increment = 1, cv = 5, percent_complete = False):
  """
  Tests a Random Forest Regerssor model with data that encoded and imputed through a pipeline object.
  All the arguments of experiment_with_Forest apply except for the isDataTable boolean, as all future
  data will be converted to a data table after the speed results found in Subsection D - Comparison
  with Gridsearch were comparable with the intended optimization output style. Additionally, there
  is the additonal preprocessor_arg and cv argument which is designated respectively for a ColumnTransformer
  and number of K-folds. If cv is set to 1, then only the mae_results without teh mae_results_sd, otherwise
  both mae_results and mae_results_sd (which represents the standard deviation of the K-fold validation), will
  be returned.
  """
  #Initializes all the needed dictionaries and ranges
  mae_results = {}
  mae_results_sd = {}
  n_estimators_range = list(range(1, n_estimators_range_arg+1, NE_increment))
  max_depth_range = max_depth_num_or_list_arg
  if percent_complete:
    #Finds total number of iterations needed to complete function
    total_num_of_iterations = len(max_depth_range)*len(n_estimators_range)
  for max_depth in max_depth_range:
    #Now max_depth will be constant while it runs through all the n_estimators, then it will increase by 1 and iterate
    for n_estimators in n_estimators_range:
      #Intitializes model and pipeline with given preprocessor, calculates MAE with dataset 
      Forest_model = initialize_Forest(n_estimators, max_depth)
      pipeline_model = initialize_Pipeline(preprocessor_arg, Forest_model)
      #If the number of K-folds is greater than 1, both the average of the folds and standard deviation is returned
      if cv > 1:
        mae_res, mae_res_sd = mae_cross_val(pipeline_model, X_arg, y_arg, cv_arg = cv)
        mae_results.setdefault(max_depth, []).append([max_depth, mae_res, n_estimators])
        mae_results_sd.setdefault(max_depth, []).append([n_estimators, mae_res_sd])
      #Otherwise, only the result of the one fold is calculated
      else:
        mae_res = mae(pipeline_model, X_arg, y_arg)
        mae_results.setdefault(max_depth, []).append([max_depth, mae_res, n_estimators])
      if percent_complete:
        #Finds the number of iterations completed by looking at indexes of n_estimators and max_depth
        num_of_iterations_completed = (n_estimators_range.index(n_estimators)+1) + (max_depth_range.index(max_depth)*len(n_estimators_range))
        num_of_iterations_completed_bef = (n_estimators_range.index(n_estimators)) + (max_depth_range.index(max_depth)*len(n_estimators_range))
        #Calculates percentage of function done, total_num_of_iterations defined at the beginning of else statement
        progress_percent = round((num_of_iterations_completed / total_num_of_iterations), 3) * 100
        progress_percent_bef = round((num_of_iterations_completed_bef / total_num_of_iterations), 3) * 100
        #Removes print if progress_precent hasn't changed
        if (progress_percent != progress_percent_bef):
          print(str(progress_percent) +'%')
  if cv > 1:
    return mae_results, mae_results_sd
  else:
    return mae_results
def average_SD_pipelineCV_Forest(mae_results_sd):
  """
  Finds the average mae value at a specifc n_estimators over all max_depth values.
  Returns a DataFrame with the columns 'n_estimators' and 'Standard Deviation'.

  *** Numpy as np and Pandas as pd dependencies ***
  """
  #Finds the values, converts to a numpy array, and initializes return dictionary
  (key_values, data_unzipped) = zip(*mae_results_sd.items())
  raw_sd = np.array(data_unzipped)
  pruned_sd = {'n_estimators':[], 'Standard Deviation':[]}
  #Iterates through rows, which are separated based on n_estimators
  for n_estimators in range(0, len(raw_sd[0])):
    #Finds average mean across all max_depth arrays with constant n_estimators
    avg_at_n_estimators = raw_sd[:,n_estimators,1].mean()
    #Adds the n_estimators and respective average mae to dictionary
    pruned_sd['n_estimators'].append(raw_sd[0,n_estimators,0])
    pruned_sd['Standard Deviation'].append(avg_at_n_estimators)
  #Converts to a DataFrame with both columns set as an index
  return pd.DataFrame(pruned_sd, index = None)

### Abbreviated Functions
### ---------------------
### For information consult Section II on Taxonomy of Functions
def ewpi(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, 
                                      preprocessor_arg, NE_increment = 1, cv = 5, percent_complete = False):
  """
  Consult experiment_with_pipelineCV_Forest for documentation.
  """
  return experiment_with_pipelineCV_Forest(n_estimators_range_arg, max_depth_num_or_list_arg, X_arg, y_arg, 
                                           preprocessor_arg, NE_increment = NE_increment, cv = cv, percent_complete = percent_complete)
def iPi(preprocessor_arg, model_arg):
  """
  Consult initialize_Pipeline for documentation.
  """
  return initialize_Pipeline(preprocessor_arg, model_arg)
  
#Section VI |
#-----------

def experiment4D_with_XGB(n_estimators_range_arg, max_depth_num_or_list_arg, learning_rate_range_arg, X_arg, y_arg, preprocessor_arg,
                                      NE_increment = 1, cv = 5, percent_complete = False, learning_rate_divisor = 100):
  """
  Enables trivariate hyperparameter optimization of a XGB Regressor. The first three arguments define the range
  of the n_estimators, max_depth, and learning_rate. The next two define data, and the next the preprocessor/
  ColumnTransformer object. The NE_increment changes the increment of n_estimators as the range argument is
  an int. The cv determines number of K-folds. Percent_complete offers console dialog on the status of the
  function. Learning_rate_divisor is what the range entered in the learning_rate_range argument is divided
  by; for instance, range(1,100) with the default learning_rate_divisor would test a learning rate of 
  .01 to .99.
  """
  #Sets the ranges of the hyperparamters
  mae_results = {}
  mae_results_sd = {}
  n_estimators_range = list(range(1, n_estimators_range_arg+1, NE_increment))
  max_depth_range = max_depth_num_or_list_arg
  learning_rate_range = [rate / learning_rate_divisor for rate in learning_rate_range_arg]
  if percent_complete:
    #Finds total number of iterations needed to complete function
    total_num_of_iterations = len(max_depth_range)*len(n_estimators_range)*len(learning_rate_range)
  for max_depth in max_depth_range:
    #Now max_depth will be constant while it runs through all the n_estimators, then it will increase by 1 and iterate
    for learning_rate in learning_rate_range:
      for n_estimators in n_estimators_range:
        #Intitializes model and pipeline with given preprocessor, calculates MAE with dataset, 
        XGB_model = initialize_XGB(n_estimators, learning_rate, max_depth)
        pipeline_model = initialize_Pipeline(preprocessor_arg, XGB_model)
        #Determines whether cross-validation is performed
        if cv > 1:
          mae_res, mae_res_sd = mae_cross_val(pipeline_model, X_arg, y_arg, cv_arg = cv)
          mae_results.setdefault(max_depth, []).append([max_depth, mae_res, n_estimators, learning_rate])
          mae_results_sd.setdefault(max_depth, []).append([n_estimators, learning_rate, mae_res_sd])
        else:
          mae_res = mae(pipeline_model, X_arg, y_arg)
          mae_results.setdefault(max_depth, []).append([max_depth, mae_res, n_estimators, learning_rate])
        #Calculates how many iterations are completed and how many total, returning the ratio as a percentage
        if percent_complete:
          #Finds the number of iterations completed by looking at indexes of n_estimators, max_depth, leanring_rate
          max_depth_loop_num = len(n_estimators_range)*len(learning_rate_range)*max_depth_range.index(max_depth)
          learning_rate_num = len(n_estimators_range)*learning_rate_range.index(learning_rate)
          num_of_iterations_completed = n_estimators_range.index(n_estimators) + 1 + learning_rate_num + max_depth_loop_num
          num_of_iterations_completed_bef = n_estimators_range.index(n_estimators) + learning_rate_num + max_depth_loop_num
          #Calculates percentage of function done, total_num_of_iterations defined at the beginning of else statement
          progress_percent = round((num_of_iterations_completed / total_num_of_iterations), 3) * 100
          #Calculates the percentage before
          progress_percent_bef = round((num_of_iterations_completed_bef / total_num_of_iterations), 3) * 100
          #Removes print if progress_precent hasn't changed
          if (progress_percent != progress_percent_bef):
            print(str(progress_percent) +'%')
  #Returns the standard deviation results if cross-validation was performed
  if cv > 1:
    return mae_results, mae_results_sd
  else:
    return mae_results
def for_4D_plot_XGB(experiment_with_XGB_res):
  """
  This converts the data to a format that can be used for a four dimensional
  graph. The format is a dictionary with the keys 'max_depth', 'mae', 'n_estimators',
  'learning_rate' and two-dimensional matrices stored in the values. It searches for
  the lowest max_depth value acros data with the same learning_rate and n_estimators
  and creates a dataset based on all of these values.
  """
  #Locates all the values and places them into a numpy array
  (key_values, data_unzipped) = zip(*experiment_with_XGB_res.items())
  raw_4D = np.array(data_unzipped)

  #List will "shuttle values" to plottable_4D before being erased after each for loop
  shuttle_list = []
  #Stores all the results from shuttle_list
  plottable_4D = []
  #Program will recognize the number of unique n_estimators
  unique_NE = 1
  #Finds how many unique instances of n_estimators without needing a user input
  while raw_4D[0,0,2] != raw_4D[0, unique_NE,2]:
    unique_NE += 1
  #Iterates through all the data collected in the experiment_with_XGB
  for t in range(0, len(raw_4D[0])):
    #Locates the lowest min value with learning_rate and n_estimators constant, but max_depth varies
    min_mae = min(raw_4D[:,t,1])
    #Finds the indices of this mae value 
    i, j, k = np.where(raw_4D == min_mae)
    #If there two or more mae values that are equally the lowest, then searches for lowest max_depth
    if len(i) > 1:
      jk_index = 0
      still_searching = True
      for i_index in range(0, len(i)):
        if still_searching:
          if raw_4D[i[i_index], j[jk_index], k[jk_index]] in raw_4D[i,j,:]:
            i, j, k = i[i_index], j[jk_index], k[jk_index]
            still_searching = False
          jk_index += 1
    #Adds this mae value with the lowest max_depth to the shuttle
    shuttle_list.append(list(raw_4D[i,j,:].flatten()))
    #When all the n_estimators vals in the range have been searched, the shuttle list drops it off at plottable_4D
    if (unique_NE - 1) == (t % unique_NE):
      plottable_4D.append(shuttle_list)
      shuttle_list = []
  #Following a conversion to a numpy, values will be transposed to enable it to graphed in a 3D plot, and these values will be stored in a dictionary
  pruned_4D = np.array(plottable_4D)
  max_depth_vals = pruned_4D[0:,0:,0].T
  mae_vals = pruned_4D[0:,0:,1].T
  n_estimators_vals = pruned_4D[0:,0:,2].T
  learning_rate_vals = pruned_4D[0:,0:,3].T
  return {'max_depth':max_depth_vals,'mae':mae_vals,'n_estimators':n_estimators_vals,'learning_rate':learning_rate_vals}
def optimize_XGB(DataTable, is_4D = False, test_max_depth = True):
  """
  Returns the lowest MAE value and parameters attendant including learning_rate, n_estimators, and max_depth.
  If the function experiment4D_with_XGB was used, set is_4D to True, otherwise simply insert what was returned
  from experiment_with_XGB function.
  """
  #Converts dictionary to list of mae values (mae_results)
  all_vals = np.array(list(DataTable.values()))
  mae_results = list(all_vals[0:,0:,1].flatten())
  max_depth_results = list(all_vals[0:,0:,0].flatten())
  n_estimators_results = list(all_vals[0:,0:,2].flatten())
  learning_rate_results = list(all_vals[0:,0:,3].flatten())

  #Finds the loewst MAE value in the list of mae_results
  min_mae = min(mae_results)
  #Locates the index of the lowest MAE value
  min_mae_index = mae_results.index(min_mae)
  opt_n_estimators = n_estimators_results[min_mae_index]
  opt_max_depth = max_depth_results[min_mae_index]
  opt_learning_rate = learning_rate_results[min_mae_index]
  
  #Sorts optimization results based on experiment
  if is_4D:
    return {'Optimal max_depth':int(opt_max_depth), 'Optimal n_estimators':int(opt_n_estimators), 'Optimal MAE':min_mae,
          'Optimal learning_rate':opt_learning_rate}
  elif test_max_depth:
    return {'Optimal max_depth':int(opt_max_depth), 'Optimal n_estimators':int(opt_n_estimators), 
            'Optimal MAE':min_mae, 'Constant learning_rate':opt_learning_rate}
  else:
    return {'Constant max_depth':int(opt_max_depth), 'Optimal n_estimators':int(opt_n_estimators), 
            'Optimal MAE':min_mae, 'Optimal learning_rate':opt_learning_rate}
def for_3D_plot_XGB(experiment_with_XGB_res, test_max_depth = True):
  """
  Converts the data from the function experiment_with_XGB into plottable 3D data. If the function
  tested n_estimators over a changing learning_rate instead of a max_depth, then make sure to 
  change test_max_depth to False. For the most comprehensive documentation on the function's 
  modus operandi consult for_3D_plot_Forest.
  """
  #Separates the keys from the values, remember all the needed data is in the values
  #Needed data = [max_depth,mae_res,n_estimators]
  (key_values, data_unzipped) = zip(*experiment_with_XGB_res.items())
  #Converted data_unzipped to an numpy array, where then data is sliced to max_depth
  #mae_res,n_estimators accordingly, transposed, and then stored accordingly
  data_array = np.array(data_unzipped)
  max_depth_or_learning_rate_vals = data_array[0:,0:,0].T
  mae_vals = data_array[0:,0:,1].T
  n_estimators_vals = data_array[0:,0:,2].T
  if test_max_depth:
    A_data = {'Max Depth': max_depth_or_learning_rate_vals, 'MAE':mae_vals, 'Number of Trees':n_estimators_vals}
  else:
    A_data = {'Learning Rate': max_depth_or_learning_rate_vals, 'MAE':mae_vals, 'Number of Trees':n_estimators_vals}
  return A_data
def interactive_surface_XGB(title, A_data):
  """
  ****
  Creates an interactive surface plot with the desired formatting based on the data inputted.

  Dependencies
  *** plotly.graph_objects as go ***
  """
  #Checks to see which parameter, either max_depth or learning_rate
  if 'Max Depth' in A_data.keys():
    #Creates surface figure based on data arguments
    fig = go.Figure(data=[go.Surface(z = A_data['MAE'], x = A_data['Max Depth'], y = A_data['Number of Trees'])])
    #Formats figure title, axis titles, dimesnions, and margins
    fig.update_layout(title= title + ' Interactive Surface Plot | Optimization of XGBR Model', autosize=True,
                      scene = dict(
                      xaxis_title='Max Depth of Each Tree',
                      yaxis_title='Number of Trees',
                      zaxis_title='Mean Absolute Error'),
                      width=1100, height=800,
                      margin=dict(l=65, r=50, b=65, t=90))
  else: 
    #Creates surface figure based on data arguments
    fig = go.Figure(data=[go.Surface(z = A_data['MAE'], x = A_data['Learning Rate'], y = A_data['Number of Trees'])])
    #Formats figure title, axis titles, dimesnions, and margins
    fig.update_layout(title= title + ' Interactive Surface Plot | Optimization of XGBR Model', autosize=True,
                      scene = dict(
                      xaxis_title='Learning Rate',
                      yaxis_title='Number of Trees',
                      zaxis_title='Mean Absolute Error'),
                      width=1100, height=800,
                      margin=dict(l=65, r=50, b=65, t=90))    
  fig.show()
def comparison_plot_surface_XGB(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                   A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0,
                                   a_xshift = 0, b_xshift = 0):
  """
  Plots two surface plots with the desired formatting based on the data inputted.

  Dependencies
  *** matplotlib as mpl ***
  *** matplotlib.pyplot as plt ***
  """
  #Sets parameters for figure quality and text font (for consistency across notebook)
  mpl.rcParams['figure.dpi'] = 300
  plt.rcParams["font.family"] = "serif"

  #Additional step needed to change the labels and title
  sanserif = {'fontname':'serif'}

  #Sets size, defines 3d plot
  fig1=plt.figure(figsize=(20,15))
  ax = plt.axes(projection='3d')
  
  #Plots all the 3D data to a surface plot
  #Sets all labels and title with desired font size and label padding, and viewing angle
  ax.plot_surface(A_data['Max Depth'], A_data['Number of Trees'], A_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =a_alpha, antialiased=True)
  ax.plot_surface(B_data['Max Depth'], B_data['Number of Trees'], B_data['MAE'], rstride=1, cstride=1, 
                  cmap='viridis', edgecolor='none', alpha =b_alpha, antialiased=True)
  ax.set_title(title + ' Surface Plot | Optimization of XGBR Model', fontdict = sanserif, fontsize=16, pad=60)
  ax.set_ylabel('Number of Trees', fontdict = sanserif, fontsize= 12, labelpad=10)
  ax.set_zlabel('Mean Absolute Error', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.set_xlabel('Max Depth of Each Tree', fontdict = sanserif, fontsize=12, labelpad=10)
  ax.text(min(A_data['Max Depth'].flatten()) - min(A_data['Max Depth'].flatten())*.01, 
          max(A_data['Number of Trees'].flatten()) + a_xshift, 
          min(A_data['MAE'].flatten()) + min(A_data['MAE'].flatten()) *.005 + a_label_sep,
          A_label, fontsize = 12, style='italic')
  ax.text(min(B_data['Max Depth'].flatten()) - min(B_data['Max Depth'].flatten())*.01, 
          max(B_data['Number of Trees'].flatten()) + b_xshift, 
          min(B_data['MAE'].flatten()) + min(B_data['MAE'].flatten()) *.005 + b_label_sep,
          B_label, fontsize = 12, style='italic')  
  ax.view_init(50, 35)
def comparison_interactive_surface_XGB(title, A_data, B_data, a_alpha = .8, b_alpha = .8,
                                       A_label = '', B_label = '', a_label_sep = 0, b_label_sep = 0):
  """
  Creates two interactive surface plots with the desired formatting based on the data inputted.

  Dependencies
  *** plotly.graph_objects as go ***
  """
  #Creates surface figure based on data arguments
  fig = go.Figure(data=[go.Surface(z = A_data['MAE'], x = A_data['Max Depth'], y = A_data['Number of Trees'], 
                                   opacity=a_alpha),
                        go.Surface(z = B_data['MAE'], x = B_data['Max Depth'], y = B_data['Number of Trees'], 
                                   opacity=b_alpha, showscale=False)])
  #Formats figure title, axis titles, dimesnions, and margins
  fig.update_layout(title= title + ' Interactive Surface Plot | Optimization of XGBR Model', autosize=True,
                    scene = dict(xaxis_title='Max Depth of Each Tree',
                                 yaxis_title='Number of Trees',
                                 zaxis_title='Mean Absolute Error',
                                 annotations= [dict(showarrow=False,
                                                    x=min(A_data['Max Depth'].flatten()),
                                                    y=max(A_data['Number of Trees'].flatten()),
                                                    z=min(A_data['MAE'].flatten()),
                                                    text=A_label,
                                                    xanchor="left",
                                                    xshift=min(A_data['Max Depth'].flatten())*.05,
                                                    yshift=min(A_data['MAE'].flatten())*.001 + a_label_sep/100,
                                                    opacity=0.7
                                              ),
                                              dict(showarrow=False,
                                                   x=min(B_data['Max Depth'].flatten()),
                                                   y=max(B_data['Number of Trees'].flatten()),
                                                   z=min(B_data['MAE'].flatten()),
                                                   text=B_label,
                                                   xanchor="left",
                                                   xshift=min(B_data['Max Depth'].flatten())*.05,
                                                   yshift=min(B_data['MAE'].flatten())*.001 + b_label_sep/100,
                                                   opacity=0.7
                                              )]
                                 ),
                    width=1100, height=800,
                    margin=dict(l=65, r=50, b=65, t=90),
                    )
  fig.show()
def interactive_4Dsurface_XGB(title, A_data):
  """
  Creates an interactive surface plot with the desired formatting based on the data inputted. Expects
  a fourth dimension of 'max_depth' and will represent this with color as the z-axis, x-axis, and y-axis
  will respectively be 'mae', 'n_estimators', and 'learning_rate" within the dictionary A_data.

  Dependencies
  *** plotly.graph_objects as go ***
  """
  #Creates surface figure based on data arguments
  fig = go.Figure(data=[go.Surface(z = A_data['mae'], x = A_data['n_estimators'], y = A_data['learning_rate'],
                                   surfacecolor = A_data['max_depth'], colorbar = dict(title = 'Max Depth'))])
  #Formats figure title, axis titles, dimesnions, and margins
  fig.update_layout(title= title + ' - 4D Interactive Surface Plot | Optimization of XGBR Model', autosize=True,
                    scene = dict(
                      xaxis_title='Number of Trees',
                      yaxis_title='Learning Rate',
                      zaxis_title='Mean Absolute Error'),
                    width=1100, height=800,
                    margin=dict(l=65, r=50, b=65, t=90))
  fig.show()
def initialize_XGB(n_estimators_arg, learning_rate_arg, max_depth_arg):
  """
  Initializes an XGB Regressor to desired n_estimators, learning_rate, and max_depth.
  """
  model = XGBRegressor(n_estimators = n_estimators_arg, learning_rate = learning_rate_arg, max_depth = max_depth_arg,
                       n_jobs = 8, random_state = 0, verbosity = 0)
  return model
def experiment_with_XGB(n_estimators_range_arg, max_depth_or_learning_rate, X_arg, y_arg, preprocessor_arg,
                        NE_increment = 1, cv = 5, percent_complete = False, test_max_depth = True,
                        learning_rate_divisor = 100, default_learning_rate = .1, default_max_depth = 5):
  """
  Enables bivariate hyperparamter optimization of a XGB Regressor model. For trivariate hyperparamter optimization,
  consider using the function experiment4D_with_XGB. This enables the n_estimators to always change and either the
  max_depth or learning_rate to change with the opposite remaining constant. To change the constant variable, change
  the default_learning_rate or default_max_depth to desired value; if you wish to test max_depth, set test_max_depth
  to True, conversely set test_max_depth to False to test learning_rate. For a detailed overview of all arguments,
  look below.

  Parameters:
  * n_estimators_range_arg: same as previous experiment functions---a single integer
  * max_depth_or_learning_rate: a range(x,y,z) argument where x is the lower limit, y is the upper limit (not included)
    and z is the increment of the range
  * X_arg and y_arg: the predictors and target variable
  * preprocessor_arg: a ColumnTransformer object
  * NE_increment: increment n_estimators_range_arg
  * cv: number of K-folds
  * percent_complete: reports how much of function is completed
  * test_max_depth: defaults to True, if True, max_depth_or_learning_rate range changes the max_depth, otherwise it
    changes the the learning_rate
  * learning_rate_divisor: divides the range, if testing learning rate (test_max_depth = False), by this value. For
    instance, with a range(1,100) and default learning_rate divisor of 100, then learning_rate will be tested from
    .01 to .99.
  * default_learning_rate: what the learning_rate is if test_max_depth = True
  * default_max_depth: what the max_depth is if test_max_depth = False
  """
  #Initializes return dictionaries and sets n_estimators range
  mae_results = {}
  mae_results_sd = {}
  n_estimators_range = list(range(1, n_estimators_range_arg+1, NE_increment))
  #Finds total number of iterations
  if percent_complete:
    total_num_of_iterations = len(max_depth_or_learning_rate)*len(n_estimators_range)
  #Runs this if user wishes to test max_depth with a constant learning_rate  
  if test_max_depth:
    max_depth_range = max_depth_or_learning_rate
    for max_depth in max_depth_range:
      for n_estimators in n_estimators_range:
        #Initializes an XGB model with the default learning_rate and changing max_depth and n_estimators
        XGB_model = initialize_XGB(n_estimators, default_learning_rate, max_depth)
        #Initializes pipeline with XGB model and preprocessor stated in the argument
        pipeline_model = initialize_Pipeline(preprocessor_arg, XGB_model)
        #Determines whether K-fold validation will take place, and if so records standard deviation in addition to mae
        if cv > 1:
          mae_res, mae_res_sd = mae_cross_val(pipeline_model, X_arg, y_arg, cv_arg = cv)
          mae_results.setdefault(max_depth, []).append([max_depth, mae_res, n_estimators, default_learning_rate])
          mae_results_sd.setdefault(max_depth, []).append([n_estimators, mae_res_sd])
        #Runs if there is no K-fold validation
        else:
          mae_res = mae(pipeline_model, X_arg, y_arg)
          mae_results.setdefault(max_depth, []).append([max_depth, mae_res, n_estimators, default_learning_rate])
        #Divides the number of iterations of completed by the total number of iterations to return percentage of function completed
        if percent_complete:
          num_of_iterations_completed = (n_estimators_range.index(n_estimators)+1) + (max_depth_range.index(max_depth)*len(n_estimators_range))
          num_of_iterations_completed_bef = (n_estimators_range.index(n_estimators)) + (max_depth_range.index(max_depth)*len(n_estimators_range))
          progress_percent = round((num_of_iterations_completed / total_num_of_iterations), 3) * 100
          progress_percent_bef = round((num_of_iterations_completed_bef / total_num_of_iterations), 3) * 100
          if (progress_percent != progress_percent_bef):
            #Prints the total percentage of function completed
            print(str(progress_percent) +'%')    
  #Runs this if user wishes to test learning_rate with a constant max_depth
  else:
    learning_rate_range_arg = max_depth_or_learning_rate
    #Divides learning_rate_range by the learning_rate_divisor which defaults to 100
    #This means that a range of (1,100) with default divisor will test [.01 to .99] learning_rate
    learning_rate_range = [rate / learning_rate_divisor for rate in learning_rate_range_arg]
    for learning_rate in learning_rate_range:
      for n_estimators in n_estimators_range:
        #Initializes an XGB model with the default max_depth and changing learning_rate and n_estimators
        XGB_model = initialize_XGB(n_estimators, learning_rate, default_max_depth)
        #Initializes pipeline with XGB model and preprocessor stated in the argument
        pipeline_model = initialize_Pipeline(preprocessor_arg, XGB_model)
        #Determines whether K-fold validation will take place, and if so records standard deviation in addition to mae
        if cv > 1:
          mae_res, mae_res_sd = mae_cross_val(pipeline_model, X_arg, y_arg, cv_arg = cv)
          mae_results.setdefault(learning_rate, []).append([default_max_depth, mae_res, n_estimators, learning_rate])
          mae_results_sd.setdefault(learning_rate, []).append([n_estimators, mae_res_sd])
        #Runs if there is no K-fold validation
        else:
          mae_res = mae(pipeline_model, X_arg, y_arg)
          mae_results.setdefault(learning_rate, []).append([default_max_depth, mae_res, n_estimators, learning_rate])
        #Divides the number of iterations of completed by the total number of iterations to return percentage of function completed
        if percent_complete:
          num_of_iterations_completed = (n_estimators_range.index(n_estimators)+1) + (learning_rate_range.index(learning_rate)*len(n_estimators_range))
          num_of_iterations_completed_bef = (n_estimators_range.index(n_estimators)) + (learning_rate_range.index(learning_rate)*len(n_estimators_range))
          progress_percent = round((num_of_iterations_completed / total_num_of_iterations), 3) * 100
          progress_percent_bef = round((num_of_iterations_completed_bef / total_num_of_iterations), 3) * 100
          if (progress_percent != progress_percent_bef):
            #Prints the total percentage of function completed
            print(str(progress_percent) +'%')
  #Return result determined whether k-fold validation was performed
  if cv > 1:
    return mae_results, mae_results_sd
  else:
    return mae_results
def zoom_3D_XGB(A_data_arg, mae_upper_limit):
  """
  Allows for the interactive_4Dsurface_XGB to focus on values below a certain mae_upper_limit to enhance
  granularity of interactive graph. A_dat_arg is the return value of for_4D_plot_XGB.
  """
  #Copies data, initializes important dictionaries
  A_data = A_data_arg.copy()
  pruned_data = {}
  keys = {}
  for param in A_data_arg.keys():
    keys[param] = []

  #Filters for data rows based on if the 'mae' value is lower then mae_upper_limit
  A_data_test = A_data['MAE'] < mae_upper_limit
  for k in range(0, len(A_data_test)):
    #Clears shuttle_dict for next iteration
    shuttle_dict = {} 
    #Iterates through A_data_test at index k and appends parameters to shuttle_dict
    for i in range(0, len(A_data_test[k])):
      if A_data_test[k,i]:
        for param in keys.keys():
          shuttle_dict.setdefault(param, []).append(A_data[param][k,i])
    #Appends shuttle_values to pruned_data
    for param in shuttle_dict.keys():
      pruned_data.setdefault(param, []).append(shuttle_dict[param]) 
  return pruned_data
def zoom_4D_XGB(A_data_arg, mae_upper_limit):
  """
  Allows for the interactive_4Dsurface_XGB to focus on values below a certain mae_upper_limit to enhance
  granularity of interactive graph. A_dat_arg is the return value of for_4D_plot_XGB.
  """
  #Copies data, initializes important dictionaries
  A_data = A_data_arg.copy()
  pruned_data = {}
  keys = {'mae':[], 'n_estimators':[],
          'learning_rate':[], 'max_depth':[]}
  #Filters for data rows based on if the 'mae' value is lower then mae_upper_limit
  A_data_test = A_data['mae'] < mae_upper_limit
  for k in range(0, len(A_data_test)):
    #Clears shuttle_dict for next iteration
    shuttle_dict = {} 
    #Iterates through A_data_test at index k and appends parameters to shuttle_dict
    for i in range(0, len(A_data_test[k])):
      if A_data_test[k,i]:
        for param in keys.keys():
          shuttle_dict.setdefault(param, []).append(A_data[param][k,i])
    #Appends shuttle_values to pruned_data
    for param in shuttle_dict.keys():
      pruned_data.setdefault(param, []).append(shuttle_dict[param]) 
  return pruned_data
def test_model_XGB(model_arg, X_arg, y_arg, X_test_arg, preprocessor_arg = None):
  """
  Different from test_model function since it adds an optional preprocessor argument. Same function as 
  train_model except for the absence of a train_test_split function and no actualy-value output like val_y 
  in train_model. Used to fit an optimized ML model with the entire predictors data before predicting with
  the test predictors dataset.
  """
  if preprocessor_arg == None:
    model_arg.fit(X_arg, y_arg)
    return model_arg.predict(X_test_arg)
  else:
    pipeline_model = initialize_Pipeline(preprocessor, model_arg)
    pipeline_model.fit(X_arg, y_arg)
    return pipeline_model.predict(X_test_arg)
    
### Abbreviated Functions
### ---------------------
### For information consult Section II on Taxonomy of Functions

def iXG(n_estimators_arg, learning_rate_arg, max_depth_arg):
  """
  Consult initialize_XGB for documentation.
  """
  return initialize_XGB(n_estimators_arg, learning_rate_arg, max_depth_arg)
def e4XG(n_estimators_range_arg, max_depth_num_or_list_arg, learning_rate_range_arg,
         X_arg, y_arg, preprocessor_arg, NE_increment = 1, cv = 5, percent_complete = False,
         learning_rate_divisor = 100):
  """
  Consult experiment4D_with_XGB for documentation.
  """
  return experiment4D_with_XGB(n_estimators_range_arg, max_depth_num_or_list_arg, learning_rate_range_arg,
                               X_arg, y_arg, preprocessor_arg, NE_increment = NE_increment, cv = cv, percent_complete = percent_complete,
                               learning_rate_divisor = learning_rate_divisor)
def ewXG(n_estimators_range_arg, max_depth_or_learning_rate, X_arg, y_arg, preprocessor_arg, NE_increment = 1,
         cv = 5, percent_complete = False, test_max_depth = True, learning_rate_divisor = 100,
         default_learning_rate = .1, default_max_depth = 5):
  """
  Consult experiment_with_XGB for documentation.
  """
  return experiment_with_XGB(n_estimators_range_arg, max_depth_or_learning_rate, X_arg, y_arg, preprocessor_arg, NE_increment = NE_increment, 
                             cv = cv, percent_complete = percent_complete, test_max_depth = test_max_depth, learning_rate_divisor = learning_rate_divisor, 
                             default_learning_rate = default_learning_rate, default_max_depth = default_max_depth)
def f3XG(experiment_with_XGB_res, test_max_depth = True):
  """
  Consult for_3D_plot_XGB for documentation.
  """
  return for_3D_plot_XGB(experiment_with_XGB_res, test_max_depth = test_max_depth)
def f4XG(experiment_with_XGB_res):
  """
  Consult for_4D_plot_XGB for documentation.
  """
  return for_4D_plot_XGB(experiment_with_XGB_res)
def isXG(title, A_data):
  """
  Consult interactive_surface_XGB for documentation.
  """
  return interactive_surface_XGB(title, A_data)
def i4XG(title, A_data):
  """
  Consult interactive_4Dsurface_XGB for documentation.
  """
  return interactive_4Dsurface_XGB(title, A_data)
def cpXG(title, A_data, B_data, a_alpha = .8, b_alpha = .8, A_label = '', B_label = '',
         a_label_sep = 0, b_label_sep = 0, a_xshift = 0, b_xshift = 0):
  """
  Consult comparison_plot_surface_XGB for documentation.
  """
  return comparison_plot_surface_XGB(title, A_data, B_data, a_alpha = a_alpha, b_alpha = b_alpha, A_label = A_label, B_label = B_label,
                                     a_label_sep = a_label_sep, b_label_sep = b_label_sep, a_xshift = a_xshift, b_xshift = b_xshift)
def ciXG(title, A_data, B_data, a_alpha = .8, b_alpha = .8, A_label = '', B_label = '',
         a_label_sep = 0, b_label_sep = 0, a_xshift = 0, b_xshift = 0):
  """
  Consult comparison_interactive_surface_XGB for documentation.
  """
  return comparison_interactive_surface_XGB(title, A_data, B_data, a_alpha = a_alpha, b_alpha = b_alpha, A_label = A_label, B_label = B_label,
                                            a_label_sep = a_label_sep, b_label_sep = b_label_sep, a_xshift = a_xshift, b_xshift = b_xshift)
def oXG(DataTable, is_4D = False, test_max_depth = True):
  """
  Consult optimize_XGB for documentation.
  """
  return optimize_XGB(DataTable, is_4D = is_4D, test_max_depth = test_max_depth)
def z3XG(A_data_arg, mae_upper_limit):
  """
  Consult zoom_3D_XGB for documentation.
  """
  return zoom_3D_XGB(A_data_arg, mae_upper_limit)
def z4XG(A_data_arg, mae_upper_limit):
  """
  Consult zoom_4D_XGB for documentation.
  """
  return zoom_4D_XGB(A_data_arg, mae_upper_limit)
