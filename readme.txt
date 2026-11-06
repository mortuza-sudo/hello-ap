3 version and 3 tag

Git repo: https://github.com/mortuza-sudo/hello-ap.git


git clone https://mortuza-su:token@github.com/mortuza-sudo/hello-ap.git hello-app
Cloning into 'hello-app'...
warning: You appear to have cloned an empty repository.


$ cd hello-ap

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (main)
$ nano logic.py

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (main)
$ nano app.py

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (main)
$ nano test_logic.py

 mkdir -p .github/workflows/

nano main.yml

nano requirements.txt

 git add .

 git commit -m "Version 1: hello world with CI v4"

git push


git tag -a v1.0 -m "version 1"

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (main)
$ git push origin --tags
Enumerating objects: 1, done.
Counting objects: 100% (1/1), done.
Writing objects: 100% (1/1), 163 bytes | 163.00 KiB/s, done.
Total 1 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/mortuza-sudo/hello-ap.git
 * [new tag]         v1.0 -> v1.0


 git checkout -b version2


git add .
warning: in the working copy of 'app.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'logic.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'test_logic.py', LF will be replaced by CRLF the next time Git touches it

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version2)
$ git commit -m "version 2: CI"
[version2 9b2c595] version 2: CI
 3 files changed, 13 insertions(+), 6 deletions(-)

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version2)
$ git push
fatal: The current branch version2 has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin version2

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.


CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version2)

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version2)
$ git push --set-upstream origin version2
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 20 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 625 bytes | 625.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'version2' on GitHub by visiting:
remote:      https://github.com/mortuza-sudo/hello-ap/pull/new/version2
remote:
To https://github.com/mortuza-sudo/hello-ap.git
 * [new branch]      version2 -> version2
branch 'version2' set up to track 'origin/version2'.

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version2)
$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (main)
$ git pull


git tag -a v2.0 -m "version 2"
git push origin --tags

 git checkout -b "version 3"
fatal: 'version 3' is not a valid branch name
hint: See 'git help check-ref-format'
hint: Disable this message with "git config set advice.refSyntax false"

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (main)
$ git checkout -b version3
Switched to a new branch 'version3'

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version3)
$ git add .

CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version3)
$ git commit -m "Version 3: CI "
 
CSE-12B22L-PD16+DS_02@CSE-12B22L-PD16 UCRT64 /d/hello-ap (version3)
$ git push --set-upstream origin version3


git tag -a v3.0 -m "version 3"
git push origin --tags








