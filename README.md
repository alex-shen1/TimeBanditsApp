# Time Bandits App
Time Bandits App (name TBA) is a volunteering platform designed to encourage small-scale community cooperation by connecting those in need of assistance with those who would like to volunteer more, all while raising money for important charitable causes.

## Our Goal

Most individuals report wanting to engage in more meaningful volunteering opportunities, but many of these opportunities are too difficult to locate, require too much of a time commitment, or are too far away to be compelling. Individuals place a high premium on their own time, so we set out to build a platform that makes it as quick and easy to connect with interesting and low-commitment activities as possible, to encourage participation in the smallest-scale of community volunteering. While our platform certainly supports larger volunteering opportunities, we envision this website as the perfect platform for smaller neighborly tasks, such as helping an elderly individual shovel the snow off of their driveway, repainting the community center, or picking up litter from the local stream. 

## Rewards

We understand that individuals do not need to be rewarded to feel that volunteering time was well-spent, but we introduced several additional features to encourage users to participate frequently and remain engaged on our platform. Firstly, we closely track each user’s participation on their Profile page, and aggregate our community’s top volunteers on the Leaderboard page. We hope that this
            “Gamification” of the volunteering process will encourage users to compete with their friends and build up as high of a volunteering score as possible. Additionally, task creators have the opportunity to include a monetary reward when posting their tasks. However, there's a unique twist: upon completion of the task, that money would not go to the person who completed the task, but be be donated to a preselected charity. In this way, people can be incentivized to work on tasks that support causes they believe in; for example, someone who cares a lot about the environment might be more willing to help someone who promises to donate to an animal conservation foundation. The charities available to be selected would have to be on an approved list — here are some that we recommend to be used with the app*:

- https://www.charitywatch.org/charities/cancer-research-institute
- https://www.charitywatch.org/charities/childrens-defense-fund
- https://www.charitywatch.org/charities/partnership-for-drug-free-kids
- https://www.charitywatch.org/charities/environmental-defense-action-fund
- https://www.charitywatch.org/charities/fisher-house-foundation
- https://www.charitywatch.org/charities/animal-welfare-institute

<sub> *For simplicity and avoiding liability issues, the current build of the app does not actually send any money to anyone, but instead we have simply established the infrastructure to allow such functionality to happen. </sub>

## How It Works

Account Creation - While users are welcome to browse tasks at their leisure, we require users to create an account to post and sign up for tasks.

Browsing for Tasks - Users can view the list of available tasks on the homepage, and are encouraged to filter tasks to find the perfect volunteering opportunity.

Creating a Task - Any signed-in user can create a task. Users have the option to add a “donation amount”, which will prompt a payment through the secure Stripe payment system. Each task has a maximum capacity of volunteers that can join the task.

Profile - Users can visit their profile (and the profiles of others) to view the tasks they have created, their total hours spent volunteering, and the upcoming tasks they have signed up for.

## References

*  Title: Stripe
*  Author: John Collison and Patrick Collison
*  Date: 11/10/2020
*  Code version: 2.55.0
*  URL: https://github.com/stripe/stripe-python
*  Software License: MIT License
---
*  Title: django-mathfilters
*  Author: Danilo Bargen
*  Date: 11/10/2020
*  Code version: 1.0.0
*  URL: https://github.com/dbrgn/django-mathfilters
*  Software License: MIT License
---
*  Title: django-allauth
*  Author: Raymond Penners
*  Date: 10/1/2020
*  Code version: 0.43.0
*  URL: https://github.com/pennersr/django-allauth
*  Software License: MIT License

## The Team

Please feel free to contact us using the GitHub issues board, or you can individually reach out to any member of the team:

Luke Emanuel (4th-Year, UVA): lme4fb@virginia.edu

Dylan Fernandes (3rd-Year, UVA): dkf5gz@virginia.edu

Alex Shen (2nd-Year, UVA): as5gd@virginia.edu

Nick Ursini (4th-Year, UVA): nju3km@virginia.edu
