echo "starting up web diary"
cd ~/Desktop/PersonalProj/web_diary/
python img_shuffle.py & > /dev/null 2>&1 &
#jekyll serve --host=0.0.0.0 > /dev/null 2>&1 &
jekyll serve  > /dev/null 2>&1 &
