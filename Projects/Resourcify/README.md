<div align="center">
	
![image](https://user-images.githubusercontent.com/68388581/136546904-60d29684-018c-4d88-b7ee-3e15560b1904.png)
	
<a href="https://github.com/aanchalrakheja/Resourcify"><img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"></a>
<a href="https://github.com/aanchalrakheja/Resourcify"><img src="https://img.shields.io/badge/Built%20by-developers%20%3C%2F%3E-0059b3"></a>
<a href="https://github.com/aanchalrakheja/Resourcify"><img src="https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=yellow"></a>
<a href="https://github.com/aanchalrakheja"><img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?v=103"></a>

<a href="https://github.com/aanchalrakheja/Resourcify/graphs/contributors"><img src="https://img.shields.io/github/contributors/aanchalrakheja/Resourcify?color=brightgreen"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/stargazers"><img src="https://img.shields.io/github/stars/aanchalrakheja/Resourcify?color=0059b3"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/network/members"><img src="https://img.shields.io/github/forks/aanchalrakheja/Resourcify?color=yellow"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/issues"><img src="https://img.shields.io/github/issues/aanchalrakheja/Resourcify?color=0059b3"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed-raw/aanchalrakheja/Resourcify?color=yellow"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/pulls"><img src="https://img.shields.io/github/issues-pr/aanchalrakheja/Resourcify?color=brightgreen"></a>
<a href="https://github.com/aanchalrakheja/Resourcify/pulls?q=is%3Apr+is%3Aclosed"><img src="https://img.shields.io/github/issues-pr-closed-raw/aanchalrakheja/Resourcify?color=0059b3"></a> 


</div>

Started on **3 SEPTEMBER 2021**

Tagline - **One Stop Resource Guide for Unstoppable Learing**

### MOTIVE
Whenever we think of self-learning anything, we often struggle finding the perfect resources to study from. Be it documentations, youtube videos or courses, we always look for the tried and tested ones.
So here we decided to find a feasible solution to this problem by creating a beginner friendly website which lists down all the resources which are quite famous and tried and tested by many people.

### CURRENT FEATURES
Currently the website offers resources related to web-development - HTML, CSS and JS.
Initially on the homepage we have a roadmap for web developement which leads to the respective resources. 
The resources page can also be accessed indivisually from the navbar.
For the resources we have included some youtube links, some free courses and some documentations which helped us in our journey.

### Tech Used

<img alt="HTML5" src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img alt="CSS3" src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/> <img alt="JavaScript" src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> <img alt="Bootstrap**" src="https://img.shields.io/badge/bootstrap%20-%23563D7C.svg?&style=for-the-badge&logo=bootstrap&logoColor=white"/> 



Other Tech/Libraries

- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/) for UI
- [FontAwesome](https://fontawesome.com/) for Icons

---
### Folder Structure

![image](https://user-images.githubusercontent.com/68388581/136647197-32575e24-de96-4be4-9413-bcd4296d9025.png)

### IMPORTANT POINTS TO KEEP IN MIND WHILE CONTRIBUTING
1) Dont forget to add the links for bootstrap and fontawesome in your <head> tag.
2) To add NAVBAR to nay page, copy the code for navbar from home page(index.html) and include navbar.css and navbar.js for styling and entire functionality.(Made using bootstrap)
3) To add FOOTER to any page, copy the code for footer from Topic Store page (pages-> topic-store.html) and include footer.css for styling.
4) Add all the images to ASSETS folder only
	

### Future Scope

1) Our aim is to include as many domains as possible and provide multiple choices for resources.
2) We also plan to include a editor dashboard wherein a user can watch a youtube video and make notes side by side as well as download those notes too.
3) We also plan to add a BLOG section wherein we will be posting regular updates in the field of technology, some not so common facts and personal expieriences. This would help us build a community of like minded people.
4) We aim to include a facility of liking the resources which help people so that the resouce gets verified and is of more use for people.
5) We also look forward to taking suggestions from people about the resouces which helped them in their journey and include them in our website with due credit.


Feel free to come up with new ideas yourself.

# How to Contribute

If you think that you can add a new feature or want to fix a bug. We invite you to contribute to Makes Math Easy and make this project better. To start contributing, follow the below instructions:

1. Create a folder at your desire location (usually at your desktop).

2. Open Git Bash Here

3. Create a Git repository.

   Run command `git init`

4. Fork the [repository](https://github.com/aanchalrakheja/Resourcify).

5. Clone your forked repository of project.

```git clone
git clone https://github.com/<your_username>/Resourcify.git
```

6. Navigate to the project directory.

```
cd Resourcify
```

7. Add a reference(remote) to the original repository.

```
git remote add upstream https://github.com/aanchalrakheja/Resourcify.git
```

8. Check the remotes for this repository.

```
git remote -v
```

9. Always take a pull from the upstream repository to your main branch to keep it updated as per the main project repository.

```
git pull upstream main
```

10. Create a new branch(prefer a branch name that relates to your assigned issue).

```
git checkout -b <YOUR_BRANCH_NAME>
```

11. Perform your desired changes to the code base.

12. Check your changes.

```
git status
```

```
git  diff
```

13. Stage your changes.

```
git add . <\files_that_you_made_changes>
```

14. Commit your changes.

```
git commit -m "relevant message"
```

15. Push the committed changes in your feature branch to your remote repository.

```
git push -u origin <your_branch_name>
```

16. To create a pull request, click on `compare and pull requests`.

17. Add an appropriate title and description to your PR explaining your changes.

18. Click on `Create pull request`.

Congratulations🎉, you have made a PR to the Makes Math Easy.
Wait for your submission to be accepted and your PR to be merged by a maintainer.

If you have any doubts please let us know in the comments.

### BE OPEN!

---

### This project is a part of the following Open Source Program
<table style="width:80%;background-color:white;border-radius:30px;">
<tr>
  <td>

  ![Hacktoberfest-2021](https://user-images.githubusercontent.com/60106112/135565291-3c98348f-36f8-4b9a-b7b4-e365c72718d2.png)
  </td>
  </tr>
</table>


