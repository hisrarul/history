ssh demo@13.126.117.57
password: demo

mkdir israrul
cd israrul

mkdir project1
ls
cd project1/
ls
git init
ls -la
echo "This is my first class to git" > file1.txt
ls
cat file1.txt
git status
git add file1.txt
git status
git commit -m "created file1.txt"


cd israrul/
ls
mkdir project2
cd project2/
git init
echo "This is file1" > file1.txt
git status
git add file1.txt
git status
git commit -m "created file1.txt"
git status
top
cd ..
ls
cd project1/
ls
git remote add origin https://github.com/4iglance/project1.git
git push -u origin master
clear
echo "This is file2" > file2.txt
git status
git add file2.txt
git status
git commit -m "created file2.txt"
git push origin master 


git branch featureA
git branch -a
git branch -D featureA
git branch -a
ls
git checkout -b featureA
ls
git status
git checkout master
git branch -a
git checkout featureA
git branch -a


git branch featureA
git branch -a
git branch -D featureA
git branch -a
ls
git checkout -b featureA
ls
git status
git checkout master
git branch -a
git checkout featureA
git branch -a
history
git branch -a
git log
cd israrul/
clear
ls
cd project1
ls
git log
echo "This is file 3" > file3.txt
ls
git status
git stash -u
git checkout master
ls
echo "This is file4" > file4.txt
git status
git add file4.txt
git commit -m "created file4.txt"
git checkout featureA
git stash pop
git add file3.txt
git commit -m "created file3.txt"
git log
git revert f61f608456b2e967cbce5822e1dc5603e3145251(commit id)
ctrl + x (To save the changes)
ctrl + o (To exit from nano editor)
git log


git branch -a
ls
cat file3.txt
echo "This is third line in file3" >> file3.txt
cat file3.txt
git add file3.txt
git commit -m "updated file3.txt"
git log
git diff 1e4b3aed8a2906cd849e08372ffa47eae3d8972e e2f32fb6396efcbcc0c
git diff e2f32fb6396efcbcc0c 1e4b3aed8a2906cd849e08372ffa47eae3d8972e


cd project1/
clear
pwd
ls
git branch -a
git log
git checkout -b featureA
ls
git status
echo "This is 3rd file in featureA branch" > file3.txt
ls
git status
git add file3.txt
git status
git commit -m "adding file3.txt"
 git config --global user.email "@gmail.com"
git config --global user.name "hisrarul"
git commit -m "adding file3.txt"
git log
git checkout master
ls
git merge featureA
ls
cat file3.txt

 mkdir project2
 cd project
 cd project2
 clear
 git status
 git init
 git status
 echo "file 1 created in master" > file1.txt
 echo "file 2 created in master" > file2.txt
 echo "file 3 created in master" > file3.txt
 git status
 git add .
 git commit -m "added 3 files in master"
 git log
 echo "file 4 created in master" > file4.txt
 git status
 git add file4.txt
 git commit -m "created file4 in master"
 git log
 echo "file 5 created in master" > file5.txt
 git status
 git add .
 git commit -m "added in file 5 in master"
 git log
 git remote add origin https://github.com/4iglance/project2.git
 git remote -v
 git push origin master
 git checkout -b test
 ls
 echo "file 6 created in master" > file6.txt
 git status
 git add .
 git commit -m "adding a new file 6 in test branch"
 git checkout master
 echo "file 7 created in master" > file7.txt
 git add .
 git commit -m "adding file 7 in master"
 echo "file 8 created in master" > file8.txt
 git add .
 git commit -m "adding file 8 in master"
 git log
 git push origin master
 git branch -a
 git checkout test
 git log --graph --pretty=oneline
 git log --graph
 clear
 git branch -a
 git log --graph
 ls
 git status
 git checkout master
 ls
 git log --graph
 git checkout test
 git log --graph --pretty=oneline
 git rebase master
 git log --graph --pretty=oneline


git pull origin master
ls
cat file6.txt
git merge test
vi file6.txt
cat file6.txt
git merge test
git status
git add file6.txt
git merge test
git commit -m "merge conflict"
git merge test
echo "We are going to explore merge conflict from github.com byy creating a file in master branch" >> file9.txt
echo "Let's do this" >> file9.txt
cat file9.txt
git checkout test
ls
echo "We are going to explore merge conflict from github.com byy creating a file in master branch" >> file9.txt
echo "She is beautiful" >> file9.txt
echo "She is beautiful with her wonderful thoughts" >> file9.txt
git add .
git commit -m "added file9.txt"
git push origin test
git checkout master
git status
git push origin master
ls
git status
echo "We are going to explore merge conflict from github.com byy creating a file in master branch" >> file9.txt
echo "Let's do this" >> file9.txt
ls
git status
git add file9.txt
git commit -m "created file9.txt"
git push origin master
