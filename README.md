# Guiafertil: Software for Exploratory Analysis and Prediction of the Productivity Threshold in Soybean Cultivation Using Artificial Intelligence Techniques

###### Abstract

Currently, the recommendation criteria used by agronomists are inconsistent due to the lack of calibration research that accurately determines the ideal amount of agricultural inputs to be applied to soybean crops, considering specific attributes such as soil, climate, altitude, and planting system. Understanding the relationship between these factors and being able to estimate productivity is essential to improve calculations, calibrate recommendations, and promote the sustainable advancement of agricultural practices. In this context, the Guiafertil software offers a solution by using artificial intelligence to analyze the interactions between these attributes for soybean crop management, providing a reliable estimate of productivity.

###### Keywords:

Productivity
Soybean Cultivation
Neural Network
Linear Regression
SVR
Random Forest


#### 1.	Motivation and significance

Soils with inadequate chemical characteristics, such as high acidity, elevated levels of exchangeable aluminum, and deficiencies in calcium and magnesium, among others, negatively affect the efficiency of agricultural management [1]. For plants, the main damages caused by acidic soils are related to aluminum and manganese phytotoxicity, as well as calcium and magnesium deficiencies in the soil [2]. On the other hand, once these issues are identified and corrected, the soil can present great agricultural potential [1].
When making recommendations for soybean crop management, agronomists must consider several parameters, such as the expected productivity, optimal soil nutrient levels, appropriate minimum and maximum average temperature ranges, ideal rainfall amounts, and the recommended doses of macro and micronutrients. Proper crop management is essential for accurately estimating productivity and ensuring the economic viability of agricultural practices. Ribeiro [1] emphasizes the need for "calibration" studies that more precisely indicate the ideal amount of agricultural inputs to be applied, taking specific attributes into account.
In this context, the Guiafertil software uses artificial intelligence to analyze the influence of soil chemical attributes, climatic conditions, and fertilization practices on soybean productivity, enabling the prediction of its productivity threshold.
Various machine learning techniques have been applied to agriculture to optimize crop productivity analysis and prediction. In the study by Shammi [3], a multispectral image generator mounted on an unmanned aerial vehicle was used to capture images in five spectral bands for monitoring soybean growth in the field, enabling yield prediction. Different machine learning algorithms were employed for this purpose.
Santos [4] investigated the performance of the Random Forest algorithm in predicting soybean productivity based on datasets obtained from traditional agricultural management experiments, evaluating the relationship between cover cropping systems and soybean yield.
Joshi [5] developed models based on satellite remote sensing and artificial intelligence (AI) to predict soybean yield. 
Pejak [6] explored the application of machine learning in predicting soybean productivity by training models with multispectral images from the Sentinel-2 satellite and soil parameters. Similarly, Khalila [7] analyzed Neural Network models aimed at estimating grain yield, evaluating both the multispectral data sources used and the performance criteria of the proposed models.
Guimarães [8] investigated machine learning-based approaches for predicting soybean productivity, with an emphasis on Neural Networks. The study compared the performance of Multilayer Perceptron, Random Forest, and Extreme Gradient Boosting models against a conventional agrometeorological model for yield estimation.
Leal [9] evaluated the effectiveness of using soil attributes in modeling second-crop maize productivity by employing a hybrid approach combining regression and Artificial Neural Networks to define site-specific management zones. Soares [10] developed an intelligent system based on Artificial Neural Networks to estimate corn production in the central region of Rio Grande do Sul, using morphological variables. Vriesmann [11] investigated the application of artificial intelligence techniques to analyze soil physicochemical data in order to predict soybean productivity, using Decision Trees and Genetic Algorithms. Bucene [12] proposed the classification of apparent soil fertility through Artificial Neural Networks, analyzing attributes such as pH, CEC (Cation Exchange Capacity), base saturation, and levels of phosphorus, magnesium, and potassium.
In this context, the Guiafertil software aims to fill a gap by integrating multiple agronomic factors into a single soybean productivity prediction model. The studies mentioned above analyze only spectral data, soil parameters, or climate in isolation. This project simultaneously considers the interactions among soil attributes, climate, altitude, planting system, and fertilizers. This broader approach allows for more accurate estimates and a comprehensive understanding of the factors that impact productivity.
An important distinguishing feature of the software is the transformation of predictive models into a practical and accessible tool. Instead of being limited to academic analysis of the results, this project proposes a graphical user interface that facilitates the use of AI models. This aspect contributes to the transfer of scientific knowledge to the productive sector.
The Guiafertil environment was developed in Python [13], integrating the SQLite3 database [14] and the PySide6 library [15] to create intuitive and functional graphical interfaces focused on agricultural information management. The software is composed of four main modules: User Registration, Producer Registration, Attribute Registration (including soil analysis data, climatic information, applied fertilization, average productivity achieved, and exploratory productivity analysis), and the Productivity Prediction Environment, which uses a variety of supervised learning algorithms for predictions, such as Neural Networks, Linear Regression, Support Vector Regression (SVR), and Random Forest.
Figure 1 shows the flowchart of the Guiafertil software
![](https://raw.githubusercontent.com/dariosilvamelo/guiafertil/main/Figure_1.png)

#### 2.	Software Description

Due to the reliability of the data, the dataset used in this study was extracted from the Champions Cases of the Brazilian Soybean Strategic Committee (CESB) [16]. 
Figure 2 shows the data entry screen.
![](https://raw.githubusercontent.com/dariosilvamelo/guiafertil/main/Figure_2.png)

Data preprocessing is a fundamental step in machine learning projects, with the primary goal of improving data quality and, consequently, the performance of the proposed model.
The preprocessing steps performed in this project included handling missing data, encoding categorical variables, data scaling, and splitting the dataset into training and testing sets.
Another essential aspect before training the machine learning models is the ability to set global randomness in Python and NumPy, as well as to define a random seed to ensure training reproducibility.
Grus [17] describes the artificial neural network as a predictive model inspired by brain dynamics, consisting of a series of interconnected neurons. Each neuron analyzes the outputs of the neurons connected to it, performs a calculation, and then either fires (if the calculated value exceeds a threshold) or does not fire (if it does not exceed the threshold). 
In this project, the TensorFlow and Keras libraries [18] were used to build a sequential neural network model that defines its architecture, specifies the optimizer, the loss function, and the evaluation metrics.
The loss function in the training of machine learning models is used to quantify the error between the model's predictions and the actual values. This function guides the learning process by helping the optimization algorithm adjust the model’s weights to minimize the errors.
The performance metric, once the model has been trained, is used to evaluate its performance on a validation or test dataset. In this context, it is not directly involved in adjusting the model’s weights, but rather in measuring how well the model has learned to predict the desired values.
The Adam optimizer is the algorithm responsible for adjusting the neural network’s weights during training in order to minimize the loss function. 
The train_test_split method [19] from the scikit-learn library is used to split the dataset, extracted from CESB’s successful case studies, into two subsets: 80% for model training and 20% for evaluation. 
Mueller [20] defines linear regression as a straight line that fits a series of x/y coordinates, determining the position of a data point. Data points are not always exactly on the line, but it shows where they would lie in a perfect world of linear coordinates. Using this line, it is possible to predict the value of y given a known value of x. When there is only one predictor variable, it is called simple linear regression; when there are multiple predictors, it is referred to as multiple linear regression.
The LinearRegression class [21] from the sklearn.linear_model module is an implementation of both simple and multiple linear regression. In this study, it was used to model the relationship between a dependent variable and one or more independent variables through a linear equation.
Support Vector Machines (SVM) are a machine learning technique widely applied in classification and regression tasks. Géron [22] explains that Support Vector Regression, or SVR, is the regression variant of SVM, used to model relationships between variables in predictive scenarios. Unlike traditional linear regression, SVR not only fits a line to represent the data but also introduces the concept of an ε-insensitive margin, which defines a tolerance band around the regression line within which deviations are not penalized. This margin establishes an interval where the differences between observed and predicted values are considered acceptable and do not impact the model’s objective function. Data points that fall within the ε margin are treated as sufficiently close to the prediction and thus do not influence model optimization. In contrast, points outside the margin are called support vectors, as they play a critical role in defining the regression line. These support vectors directly influence the model’s adjustments, forcing it to account for significant deviations. The SVR class used in this project is part of the sklearn.svm library [23], which provides the regression implementation of the SVM algorithm.
Géron [22] explains that aggregated predictions often outperform the prediction of a single expert, a phenomenon known as the "wisdom of the crowd." In this context, a group of predictors tends to produce better results than the best individual predictor. This set of combined predictions is referred to as an ensemble, and the learning technique that leverages this concept is known as an ensemble method. Random Forest is a machine learning algorithm based on an ensemble of decision trees. It combines multiple trees to improve the model’s accuracy and generalization. This method belongs to the ensemble category and can be used for both classification and regression tasks.
The RandomForestRegressor class [24] used in this project from the scikit-learn library is an implementation of the Random Forest algorithm designed for regression problems. This technique employs an ensemble of decision trees to estimate a continuous value, combining the outputs of multiple trees to produce more robust and accurate predictions.
The dataset used in this project, extracted from the Champions Cases of CESB, consisted of 37 records, with 80% allocated for training and 20% for testing.
The parameters used for training the neural network, linear regression, SVR, and random forest models are described in Table 1 below. Parameters that were not explicitly configured retained the default values of their respective classes.

##### Table 1  
**Parameter settings for the neural network, linear regression, SVR, and random forest models.**

| Model             | Parameter           | Value           |
|------------------|---------------------|-----------------|
| **Neural Network** | epochs              | 160             |
|                  | batch_size          | 5               |
|                  | learning_rate       | 0.0001          |
|                  | kernel_initializer  | 42 (seed value) |
| **Linear Regression** | fit_intercept     | True            |
|                  | normalize           | False           |
|                  | copy_X              | True            |
|                  | n_jobs              | None            |
|                  | random_state        | 42 (seed value) |
| **SVR**          | kernel              | 'rbf'           |
|                  | C                   | 1.0             |
|                  | epsilon             | 0.1             |
|                  | degree              | 3               |
|                  | random_state        | 42 (seed value) |
| **Random Forest**| n_estimators        | 400             |
|                  | random_state        | 42 (seed value) |
|                  | bootstrap           | True            |

Table 2 presents the yield predictions obtained by the models.

##### Table 2  
**Prediction results obtained after training.**

| **Neural Network** 
|Actual Yield (yi) | Predicted Yield (ŷi) | Absolute Error (|yi – ŷi|) |
| 90.0000          | 91.0438              | 1.0438                     |
| 70.0000          | 77.4858              | 7.4858                     |
| 92.0000          | 86.4027              | 5.5974                     |
| 73.5000          | 77.1419              | 3.6419                     |
| 82.0000          | 75.6923              | 6.3077                     |
| 80.0000          | 85.1857              | 5.1857                     |
| 82.0000          | 84.3755              | 2.3755                     |
| 85.7000          | 86.4820              | 0.7820                     |

 **Linear Regression** 
|Actual Yield (yi) | Predicted Yield (ŷi) | Absolute Error (|yi – ŷi|) |
| 90.0000          | 97.3934              | 7.3934                     |
| 70.0000          | 85.9367              | 15.9367                    |
| 92.0000          | 97.6273              | 5.6273                     |
| 73.5000          | 70.8004              | 2.6996                     |
| 82.0000          | 70.6779              | 11.3221                    |
| 80.0000          | 69.0353              | 10.9647                    |
| 82.0000          | 75.8950              | 6.1050                     |
| 85.7000          | 87.8340              | 2.1340                     |
 
 **SVR**
|Actual Yield (yi) | Predicted Yield (ŷi) | Absolute Error (|yi – ŷi|) |
| 90.0000           | 86.5726                | 3.4274                      |
| 70.0000           | 81.2404                | 11.2404                     |
| 92.0000           | 84.6273                | 7.3727                      |
| 73.5000           | 78.8524                | 5.3524                      |
| 82.0000           | 78.8515                | 3.1485                      |
| 80.0000           | 82.3288                | 2.3288                      |
| 82.0000           | 83.5224                | 1.5224                      |
| 85.7000           | 83.6650                | 2.0350                      |

| **Random Forest**
| 90.0000           | 85.1409                | 4.8591                      |
| 70.0000           | 77.3101                | 7.3101                      |
| 92.0000           | 82.7200                | 9.2800                      |
| 73.5000           | 78.5540                | 5.0540                      |
| 82.0000           | 76.4284                | 5.5716                      |
| 80.0000           | 81.2105                | 1.2105                      |
| 82.0000           | 83.7821                | 1.7821                      |
| 85.7000           | 84.7263                | 0.9737                      |

Table 3 presents the performance metrics MEAN, MAE, RMSE, and R² for the models.

##### Table 3  
**Prediction results obtained after training.**

| Model             | MEAN (Actual) | MEAN (Prediction) | MAE   | RMSE  | R²    |
|------------------|----------------|--------------------|-------|-------|-------|
| Neural Network    | 81.90          | 82.98              | 4.05  | 4.67  | 0.56  |
| Linear Regression | 81.90          | 81.90              | 7.77  | 8.93  | -0.60 |
| SVR               | 81.90          | 82.46              | 4.55  | 5.51  | 0.39  |
| Random Forest     | 81.90          | 81.23              | 4.51  | 5.31  | 0.43  |

Table 3 presents the MEAN, MAE, RMSE, and R² metrics corresponding to the results shown in Table 2, for the models used. The MEAN value represents the average of actual and predicted yields, while MAE (Mean Absolute Error) indicates the average absolute error. RMSE (Root Mean Squared Error) reflects the magnitude of the errors, and the coefficient of determination R² measures how well the models explain the variance in actual yield values.
The Neural Network achieved a MAE of 4.05 and an RMSE of 4.67, making it the model with the best predictive performance, with an R² of 0.56. This result indicates that the model was able to capture significant patterns in the data, making it a promising option for yield prediction.
Linear Regression showed unsatisfactory performance, with a MAE of 7.77 and an RMSE of 8.93. The negative R² value (-0.60) indicates that the model was unable to explain the variability in the data, suggesting that its application for this type of prediction is not appropriate.
SVR yielded a MAE of 4.55 and an RMSE of 5.51, with an R² of 0.39, indicating performance inferior to the Neural Network but still better than Linear Regression. This suggests that, although SVR has learning capability, it may not be the best choice for this dataset.
The Random Forest model achieved a MAE of 4.51 and an RMSE of 5.31, with an R² of 0.43. These values indicate that Random Forest showed intermediate performance—better than SVR but inferior to the Neural Network.
The results indicate that the Neural Network was the most effective model for predicting soybean yield, presenting the lowest mean absolute error and the highest coefficient of determination. Random Forest also demonstrated reasonable performance, while SVR yielded moderate results. Linear Regression, on the other hand, failed to effectively capture the relationships between the attributes and yield.
It is essential to continuously improve prediction accuracy by expanding the dataset and fine-tuning hyperparameters as it grows, thereby ensuring greater predictive capability for applications in precision agriculture.
These analyses reinforce the importance of employing advanced machine learning techniques to optimize yield prediction in soybean cultivation, aiding in decision-making regarding input use and promoting greater sustainability in Brazilian agriculture. 

#### 3.	Illustrative Examples

Figure 3 shows the yield prediction environment during training.
![Figura 3 - Ambiente de predição do Guiafertil](https://raw.githubusercontent.com/dariosilvamelo/guiafertil/main/Figure_3.png)

Figure 4 presents the exploratory analysis environment, where the user selects the model and visualizes the yield prediction for a specific scenario based on soil attributes, climate, planting system, and fertilization.

![Figura 4 - Ambiente de análise exploratória do Guiafertil](https://raw.githubusercontent.com/dariosilvamelo/guiafertil/main/Figure_4.png)

#### 4.	Impact

There is little benefit for soybean producers in having large amounts of data on yield, soil analysis, and fertilization recommendations if these data are not effectively used to improve crop outcomes. To achieve economically advantageous productivity, decision-making must rely on a sophisticated and efficient approach. In this context, the use of machine learning techniques is an effective alternative for generating valuable information and insights.
To evaluate the quality of Guiafertil, the software’s functionalities were presented to five agricultural engineers. Afterwards, a questionnaire was applied to allow them to assess the system’s quality. Figure 5 presents the questionnaire used.
![Figura 5 - Questionário de avaliação da qualidade do Guiafertil](https://raw.githubusercontent.com/dariosilvamelo/guiafertil/main/Figure_5.png)

Figure 6 presents the chart with the results obtained from the questionnaire.
![Figura 6 - Resultados do questionário de avaliação da qualidade do Guiafertil](https://raw.githubusercontent.com/dariosilvamelo/guiafertil/main/Figure_6.png)

The chart shows that, in the opinion of the agricultural engineers consulted, Guiafertil demonstrated high technical and functional quality, with minor points of attention that can be addressed to make it even more robust and ready for field use. Such small variations are normal during validation phases and can help guide the next steps in refining the system.
The Guiafertil model presented may open doors to explore new questions such as:
•	Predictive analysis in different agricultural crops: Investigation of the model’s applicability to crops beyond soybeans, such as corn and wheat.
•	Climatic impacts on agricultural productivity: Integration of climate variables to predict how climate changes may affect crop productivity.
•	Optimization of agricultural resources: Studies on how the model can be used to optimize the use of agricultural inputs.
The dissemination of the Guiafertil software within and beyond the user group may include:
•	Within the target group:
o	Downloads and active users: If made publicly available, it is possible to monitor metrics such as the number of downloads and accesses to evaluate its reach.
o	Adoption in universities and research centers: Acceptance of the software in academia can be evidenced by publications citing it as a utilized tool.
•	Outside the target group:
o	Applications in the commercial sector: Agricultural companies can incorporate the model into platforms aimed at predictive analysis, expanding its use in business practices.
o	Interdisciplinary collaborations: The software can also be utilized by professionals from other fields, such as agricultural economists and environmental planners.
•	Commercial applications: Agricultural consulting services.
•	Creation of spin-offs: Companies may emerge based on the software, offering solutions such as platforms for productivity analysis or agricultural input optimization.

#### 5.	Conclusions

Guiafertil represents an integration of technology and agriculture, offering a tool to optimize decision-making in the agricultural sector based on predictive models. With solid statistical results and performance metrics, the software proposes practical solutions to real challenges faced by farmers, agronomists, and researchers.
Its adoption in universities, research centers, agricultural companies, and other sectors may demonstrate its potential for interdisciplinary applicability. In commercial settings, the software could open doors for the development of personalized services.
Guiafertil not only has the potential to transform the daily practices of its users but also to establish a solid foundation for future advancements in precision agriculture. It is a tool for those seeking sustainable productivity, strategic decision-making, and greater competitiveness in the agricultural sector.
Furthermore, Guiafertil can open new opportunities for the enhancement and expansion of artificial intelligence use in agriculture. Among future possibilities, the development of modules for other crops stands out, allowing the same approach to be applied to corn, wheat, cotton, and other economically important crops. Another promising evolution is the integration of remote sensing variables, incorporating satellite and drone imagery data, which could further refine yield estimates and increase the accuracy of recommendations.
The adoption of these innovations further reinforces Guiafertil's role as an ally to rural producers and agricultural consultants, providing support for data-driven decision-making. Thus, the tool not only aims to address current challenges but also paves the way for a new era of efficiency and sustainability in Brazilian agriculture.



#### References

[1] Ribeiro, Antônio Carlos; Guimarães, Paulo Tacito Gontijo; Alvarez, Victor Hugo. Recommendations for the Use of Lime and Fertilizers in Minas Gerais: 5th Approximation. Viçosa-MG: Soil Fertility Commission of Minas Gerais State – UFV, 1st edition, 1999.

[2] Reatto, Adriano; Carvalho, Arminda M.; Sanzonowicz, Cláudio; Souza, Djalma M. G.; Lobato, Edson; Galrão, Enéas Z.; Mendes, Lêda de C.; Correia, João R. C.; Silva, José E.; Andrade, Leide R. M.; Vilela, Lourival; Macedo, Manuel C. M.; Hungria, Mariangela; Lobo-Burle, Marília; Vargas, Milton A. T.; Oliveira, Sebastião A. O.; Spera, Silvio T.; Rein, Thomaz A.; Soares, Wilson Vieira. Cerrado Soil Correction and Fertilization. Brasília-DF: Embrapa Cerrados, 2nd edition, 2004.

[3] Shammi, Sadia Alam; Huang, Yanbo; Feng, Gary; Tewolde, Haile; Zhang, Xin; Jenkins, Johnie; Shankle, Mark. Application of UAV Multispectral Imaging to Monitor Soybean Growth with Yield Prediction through Machine Learning. MDPI Journal, 2024. Available at: https://www.mdpi.com/2073-4395/14/4/672. Accessed on: August 21, 2024.

[4] Santos, Letícia Bernabé; Gentry, Donna; Tryforos, Alex; Fultz, Lisa; Beasley, Jeffrey; Gentimis, Thanos. Soybean Yield Prediction Using Machine Learning Algorithms Under a Cover Crop Management System. Elsevier Journal, 2024. Available at: https://www.sciencedirect.com/science/article/pii/S2772375524000479. Accessed on: August 21, 2024.

[5] Joshi, Deepak R.; Clay, Sharon A.; Sharma, Prakriti; Rekabdarkolaee, Hossein Moradi; Kharel, Tulsi; Rizzo, Donna M.; Thapa, Resham; Clay, David E. Artificial Intelligence and Satellite-Based Remote Sensing Can Be Used to Predict Soybean (Glycine max) Yield. International Journal of Agronomy, 2023. Available at: https://acsess.onlinelibrary.wiley.com/doi/epdf/10.1002/agj2.21473. Accessed on: August 21, 2024.
[6] Pejak, Branislav; Lugonja, Predrag; Antić, Aleksandar; Panić, Marko; Pandzić, Miloš; Alexakis, Emmanouil; Mavrepis, Philip; Zhou, Naweiluo; Marko, Oskar; Crnojević, Vladimir. Soya Yield Prediction on a Within-Field Scale Using Machine Learning Models Trained on Sentinel-2 and Soil Data. MDPI Journal, 2022. Available at: https://www.mdpi.com/2072-4292/14/9/2256. Accessed on: August 21, 2024.

[7] Khalila, Z.H.; Abdullaeva, S.M. Neural Network for Grain Yield Prediction Based on Multispectral Satellite Imagery: Comparative Study. Elsevier Journal, 2021. Available at: https://www.sciencedirect.com/science/article/pii/S1877050921009625. Accessed on: August 21, 2024.

[8] Guimarães, Edson da Silva. Machine Learning Applied to Soybean Yield Prediction Using Climate and Soil Data. Master’s Thesis, University of São Paulo (USP), 2019. Available at: https://www.teses.usp.br/teses/disponiveis/55/55137/tde-09062020-123106/fr.php. Accessed on: May 3, 2023.

[9] Leal, Aguinaldo José Freitas; Miguel, Eder Pereira; Baio, Fabio H. R.; Neves, Danilo de Carvalho; Leal, Ulcilea A. S. Artificial Neural Networks in Corn Yield Prediction and Definition of Differentiated Management Sites Through Soil Data. Bragantia Journal, 2015. Available at: https://www.scielo.br/j/brag/a/mtFbmv47y9B7FkKXFF6yQHw/?lang=pt. Accessed on: May 3, 2023.

[10] Soares, Fatima Cibele; Robainam, Adroaldo Dias; Peiteru, Marcia Xavier; Russim, Jumar Luiz. Corn Yield Prediction Using Artificial Neural Networks. Ciência Rural Journal, 2015. Available at: https://www.scielo.br/j/cr/a/sWcrxhGyhvPLGKhvnCWgwbD/?lang=pt. Accessed on: May 3, 2023.

[11] Vriesmann, Leila Maria; Guimarães, Alaine Margarete; Canteri, Marcelo Giovanetti; Molin, Jose Paulo; Cataneo, Angelo; Kovalechyn, Danilo. Analysis of Results Obtained by Artificial Intelligence Techniques in Soil Productivity Data Mining. Brazilian Journal of Agrocomputing, 2004. Available at: https://agrocomputacao.deinfo.uepg.br/junho_2004/Arquivos/RBAC.pdf. Accessed on: May 3, 2023.

[12] Bucene, Luciana C.; Rodrigues, Luiz H. A. Use of Artificial Neural Networks for Soil Productivity Evaluation Aimed at Land Classification for Irrigation. Brazilian Journal of Agricultural and Environmental Engineering, 2004. Available at: https://www.scielo.br/j/rbeaa/a/vGVzBJgPGC38CKr9TCCK33n/?lang=pt. Accessed on: May 3, 2023.

[13] Zumstein, Felix. Python for Excel: A Modern Environment for Automation and Data Analysis. Rio de Janeiro-RJ: Alta Books, 1st edition, 2024.

[14] Souza, Vitor Amadeu. Introduction to SQLite, Single Volume. São Paulo-SP: Clube dos Autores, 1st edition, 2024.

[15] Fitzpatrick, Martin. Create GUI Applications with Python & Qt6. Independently published, 1st edition, 2022.

[16] Brazilian Soybean Strategic Committee (CESB). Champions Cases. [n.d.]. Available at: https://www.cesbrasil.org.br/category/cases-campeoes/. Accessed on: November 18, 2024.
[17] Grus, Joel. Data Science from Scratch: Fundamental Concepts with Python. Rio de Janeiro-RJ: Alta Books, 2nd edition, 2021.

[18] Ribeiro, Maxwell M.; Guimarães, Samuel S. Neural Networks Using TensorFlow and Keras. RE3C – Electronic Scientific Journal of Computer Science, 2018. Available at: https://revistas.unifenas.br/index.php/RE3C/article/view/231. Accessed on: October 1, 2024.

[19] Salam, Mohammed Khalaf. Optimization of Regression Models Using Machine Learning: A Comprehensive Study with scikit-learn. International Uni-Scientific Research Journal, 2024. Available at: https://www.researchgate.net/publication/384051854_Optimization_of_Regression _Models_Using_Machine_Learning_A_Comprehensive_Study_with_Scikit-learn. Accessed on: December 2, 2024.

[20] Mueller, John; Massaron, Lucas. Deep Learning for Dummies. Rio de Janeiro-RJ: Alta Books, 1st edition, 2020.

[21] Patil, Sarita; Shrirao, Nitin. Linear Regression: A Practical Implementation in Python, IJIRCCE, 2023. Available at: https://siddhantica.in/naac/criteria/Criteria_3/3.3.1/Resarch%20 Paper/Linear%20regresion%20publish%20paper.pdf. Accessed on: December 2, 2024.

[22] Géron, Aurélien. Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow. Rio de Janeiro-RJ: Alta Books, 2nd edition, 2021.

[23] Yerrabolu, Venkata Lakshmi; Kasireddy, Idamakanti Kasireddy; Jasmine, K. M.; Vamsi, T. B. Murali Krishna; N., Joshua; V. Shyam Kumar; Rao, DSNM. Performance Comparison of Random Forest Regressor and Support Vector Regression for Solar Energy Prediction. International Conference on Smart and Sustainable Energy Systems, 2024. Available at: https://iopscience.iop.org/article/10.1088/1755-1315/1375/1/012013/meta. Accessed on: December 2, 2024.

[24] Halim, Rico; Bunyamin, Hendra. Sales Analysis at Serba Ada Branch Store Using Machine Learning Algorithm. Strategi, 2023. Available at: http://strategi.itmaranatha.org/index.php/ strategi/article/view/459. Accessed on: December 2, 2024.



