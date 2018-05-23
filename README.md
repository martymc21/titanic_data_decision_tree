# titanic_data_decision_tree

Introduction
When applying Machine Learning algorithms, it's critical to always keep in mind the problem we're trying to solve. In most cases, the most accurate and robust model might be what you're looking for. But sometimes we need to actually get insights from the available data and in these cases transparent, easy to understand models like Decision Trees will greatly simplify our task.

If we need to build a model that will be directly used for some task and only show it's end results, then we don't really care about building some kind of "blackbox" if it's accurate enough (image or speech recognition for example). That's why advanced techniques such as Deep Learning or Ensemble Learning (cf. Anisotropic Kernel) are commonly used for complex tasks. But remember the KISS principle (Keep It Simple, Stupid)! Always consider the complexity/accuracy trade-off: complex techniques should only be used if they offer significant improvements. Simpler models are also less prone to over-fitting and tend to generalise better.

But if we're using Machine Learning to actually get insights from the data, "blackbox" models are almost useless and it's best to stick with simpler, transparent techniques. Let's take the case of a supermarket looking to better understand customer behaviour: the straightforward Apriori algorithm can quickly offer relevant insights like "80% of customers who bought a suit also bought a tie" so they may try to increase tie sales by offering a discount to clients buying a suit . Of course, a complex classification algorithm will do better at identifying the customers who bought a tie by taking into account more features, but is that really useful for the supermarket?

Decision Trees can also help a lot when we need to understanding the data. A good example is the traditional problem of classifying Iris flowers included in the sklearn documentation, were we can learn about the characteristics of each flower type in the resulting tree. Given their transparency and relatively low computational cost, Decision Trees are also very useful for exploring your data before applying other algorithms. They're helpful for checking the quality of engineered features and identifying the most relevant ones by visualising the resulting tree.

The main downsides of Decision Trees are their tendency to over-fit, their inability to grasp relationships between features, and the use of greedy learning algorithms (not guaranteed to find the global optimal model). Using them in a Random Forest helps mitigate some of this issues.

After this short introduction to Decision Trees and their place in Machine Learning, let's see how to apply them for the Titanic challenge. First, we're going to prepare the dataset and discuss the most relevant features. We'll then find the best tree depth to avoid over-fitting, generate the final model, and explain how to visualise the resulting tree.

Preparing the Titanic dataset
For the Titanic challenge we need to guess wheter the individuals from the test dataset had survived or not. But for our current purpose let's also find out what can the data tell us about the shipwreck with the help of a Classification Tree. Let's load the data and get an overview.
