# web diary

​	This is a web-app interface to the display, search, and view the diary entries record by [terminal-diary](https://github.com/dorisjlee/terminal-diary).The web-app runs on Jekyll and is based on [Victor Hugo's space-jekyll](https://github.com/victorvoid/space-jekyll-template), released under the MIT License.  

​	The web diary option specified as ``WEB_LOC`` path during installation of terminal-diary. (If ``WEB_LOC`` is not specified, default mode doesn't contain the web-app mode ) Terminal-diary stores all of its data  as ``terminal-notes/daily/YYYY_MM_DD.md`` in ``FILE_LOC``, for each diary entry day.In the web-diary mode, the markdown files for each daily diary is reformatted into the right Jekyll format as one post per day and copied over to ``_posts`` in ``WEB_LOC``.  This update occurs everytime when you finish writing something with the ``note`` command. The set of assigned tags for all the snippets of notes in a daily diary  stored as metadata under ``tags:``.

```
layout: post

title:  2016-10-20 Segmentation Theory, Streaming Motivation

date:  2016-10-20

tags:

- crowd
- personal
- IR
- idea
- seg
- trends

categories:

- Work


[Markdown Content copied to here]
```

 Currently, the default title for every article is _Worklog_, which means it would be hard to tell from glancing at the title what each entry is. So you need to manually rename the ``title``. I found that it's actually a useful excercise that  forces me to reflect and think of a 4~6 word summary of the gist of what I learned/did at the end of each workday. (You can also put in a convenient command in your ``.bash_profile``  : ``alias workend="cd ~/Desktop/PersonalProj/web_diary/_posts/;open ."`` to speed up  this process.)

For example: 

​	~~2016-10-20 Worklog~~

​	2016-10-20 Segmentation Theory, Streaming Motivation

On the homepage there is a dynamic gallery for the same reasons why anyone puts family/personal photos on their office desk. Since Jeykll doesn't allow dynamic updating of photo galleries, the ``img_shuffle.py`` script does a  poor-man's hack job at swapping in a new image inside a designated folder every 5 hours. It should be run continuously alongside Jekyll, as demonstrated in ``startup.sh``.



# Demo 

The homepage shows all recent posts and a photo gallery: 

![home](https://raw.githubusercontent.com/dorisjlee/remote/master/web-diary-img/homepage.png)

You can perform a spotlight search (matching titles only) on the homepage:

![search](https://raw.githubusercontent.com/dorisjlee/remote/master/web-diary-img/search.png)



This is what a sample post looks like:

![This is what a sample post would look like](https://raw.githubusercontent.com/dorisjlee/remote/master/web-diary-img/post.png)



Another view of the list of posts can be sorted by tags: 

![tag](https://raw.githubusercontent.com/dorisjlee/remote/master/web-diary-img/tags.png)

### Features To-Do

- Cannot do inline math $…$, since both inline and equation math is $$…$$ with katex, need to distinguish them.
- Imported images need to be incorporated or specify the right path to file in web-diary. Make embedding image streamline process.
- Make organized notes resulting from  ``organize`` into _post.
- Enable deeper content-based (rather than title-only) search in the homepage spotlight search