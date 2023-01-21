# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st

#get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(style='ticks', palette='Set2')

# # Bayesian in Python
#
# In this tutorial, we are going to go over basic bayesian analysis in python.
#
# ## Review
#
# __Prior p(H):__ Our prior reflects what we know about the value of some parameter before seeing data.  This could refer to previous trials and distributions.
#
# __Likelihood p(D|H)__: what is the plausibility that our data is observed, given our prior?
#
# __Posterior p(H|D):__ This is result of the Bayesian analysis and reflects all that we know about a problem (given our data and model).
#
# __Evidence p(D):__ Evidence is the probability of observing the data averaged over all the possible values the parameters can take. Also knowns as the noramlziing factor. The normalising constant makes sure that the resulting posterior distribution is a true probability distribution by ensuring that the sum of the distribution is equal to 1.
#
# Because p(D) is considered a normalizing constant we can say: $p(H|D) \propto p(D|H) * p(H)$
#
# ## Coin - Flipping Problem
#
# Let's think of these terms in the context of a coin-flipping experiment.
#
# On a standard coin, we have two sides, heads or tails.  Both of which are equally likely to show after a coin flip, or a 50% probability.
#
# In the case of a coin-flipping trials, we may want to consider this probability our prior.
#
# Let's go ahead and create our prior distribution:

# In[3]:


coin_flips_prior = np.random.binomial(n=1, p=0.5, size=1000)
print(coin_flips_prior[:5])

# In[4]:


params = np.linspace(0, 1, 100)
print(params)

# In[5]:


p_prior = np.array([np.product(st.bernoulli.pmf(coin_flips_prior, p)) for p in params])

# In[6]:


p_prior = p_prior / np.sum(p_prior)
plt.figure(1)
plt.plot(params, p_prior)
sns.despine()

# As you can see, our prior distribution peaks at 0.5 which is what our probability for our fair coin is.
#
# Now, let's introduce some observations from trials with an unfair coin.  Let's say the probability is now weight 80-20, where the probability a head is shown is 0.8.
#
# Let's create this sampling distribution:

# In[7]:


coin_flips_observed = np.random.binomial(n=1, p=0.8, size=1000)
p_observed = np.array([np.product(st.bernoulli.pmf(coin_flips_observed, p)) for p in params])
p_observed = p_observed / np.sum(p_observed)
plt.figure(2)
plt.plot(params, p_observed)
sns.despine()

# The peak for our sampling distribution is around 0.8.
#
# While our observations from our sampling distribution indicate a probability around 0.8, because our prior is 0.5, we have to assess the likelihood that these values could be observed and find our posterior distribution.
#
# Remember, $p(H|D) \propto p(D|H) * p(H)\ OR\ Posterior\ \propto Likelihood\ *  Prior$

# In[8]:


p_posterior = [p_prior[i] * p_observed[i] for i in range(len(p_prior))]
p_posterior = p_posterior / np.sum(p_posterior)
plt.figure(3)
plt.plot(params, p_posterior)
sns.despine()

# ## University of Michigan Student IQs
#
# We'll do another example where we have some prior belief about the IQ of University of Michigan students.
#
# For our prior distribution, we'll have a normal distribution with a mean IQ of 100 and a standard deviation of 10.

# In[9]:


prior_distribution = np.random.normal(100, 10, 1000)
plt.figure(4)
plt.hist(prior_distribution)
sns.despine()

# Now, let's say we are collecting some observations of student IQs which takes the shape of a normal distribution with mean 115 and standard deviation of 7.5 and want to construct our posterior distribution.
#
# In order to do this, we update our prior by calculating the mean and variance after each observation.
#
# The equations for our updated prior mean and variance are:
#
# $$Updated\ Prior\ Mean = \frac{\sigma^2_{observed}\mu + \sigma_{prior}^2x}{\sigma_{observed}^2 + \sigma_{prior}^2}$$
#
# $$Updated\ Prior\ Variance = \frac{\sigma_{observed}^2\sigma_{prior}^2}{\sigma_{observed}^2 + \sigma_{prior}^2}$$

# In[10]:


np.random.seed(5)
observed_distribution = np.random.normal(115, 10, 1000)
mu = [100] * 1000
sigma = [10] * 1000

mu[0] = (10 ** 2 * observed_distribution[0] + (10 ** 2) * 100) / (10 ** 2 + 10 ** 2)
sigma[0] = (10 ** 2 * 10 ** 2) / (10 ** 2 + 10 ** 2)

for i in range(1000):
    if i == 999:
        break
    mu[i + 1] = (sigma[i] * observed_distribution[i + 1] + (10 ** 2) * mu[i]) / (sigma[i] + 10 ** 2)
    sigma[i + 1] = (sigma[i] * 10 ** 2) / (sigma[i] + 10 ** 2)

posterior_distributions = [[]] * 20

for i in range(20):
    posterior_distributions[i] = np.random.normal(mu[i], sigma[i], 1000)

plt.figure(5)
plt.hist(prior_distribution)
plt.hist(observed_distribution, alpha=0.75)
plt.hist(posterior_distributions[14], alpha=0.5)
sns.despine()

plt.show()