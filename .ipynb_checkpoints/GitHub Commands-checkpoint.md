## When you study in your local pc or local python directory;

### What you should do to send the changes to main branch is:

- git status                   : this command will check your status
- git add .                    : this command will gather all the files
- git commit -m "SomeComment"  : you define a commment regarding your study that you want to push to main branch
- git push                     : by this command, you're even with your main repository.

### What you should do to take the canges from main branch is:
- git status                   : this command will check your status
- git fetch upstream           : you're go and get the changes on the main branch's side
- git merge upstream/main      : you're bringing the files to your local pc where github is located
- git push                     : you're sending those files to your github repository