title: 博客折腾札记
slug: myblog
date: 2015-02-14 10:00:00
tags: Skill
Summary: 记录我的博客诞生历程。

[TOC]
###说在前面

不知何时萌生了想搭个博客的念头，于是就开工了。毕竟是起步阶段，所以不想弄独立主机。后来发现Github Pages是个好方案，便选择了Jekyll。可是苦于找不到好主题，搜索许久发现[farseerfc](http://farseerfc.me)的博客风格很合胃口，于是踏上了Pelican的<del>不归路</del>……
* * *

###Pelican安装

安装pelican需要python等等，具体教程网上能搜索到，因此不再赘述。
* * *

###初步使用

安装完pelican后，用markdown等语法写篇文章放到`~/contents`里，然后输入以下命令

    :::make
    make html
    make serve


然后打开浏览器输入`localhost:8000`，你就能看到一个初生的<del>巨丑无比</del>的博客了，不过不要担心，它是只**丑小鸭**，很快就会像天鹅般美丽。
* * *

###主题配置

当初选择pelican就是因为farseerfc的主题好看（<del>这个看脸的世界</del>），所以这里以那个主题为依据开展教程。

那个主题名叫`pelican-bootstrap3`，简而言之就是用默认主题加上material design后而成，瞬间就土鸡变凤凰。不过farseerfc的是多语言站，使用了`i18n_subsites`插件，所以需要相应地配置一下。

方法一：找到主题文件夹下的templates，把里面的html文件夹里的`tran`和`gettext`标签全部删掉，然后就能不使用`i18n_subsites`插件，不过那样界面就是英文的。

方法二：在单语言下使用插件。需要注意以下几点：

1、配置好pelicanconf.conf以下项目

    :::python
    DEFAULT_LANG = 'zh'
    LOCALE = u'zh_CN.utf8'
    DATE_FORMATS = u"%y年%m月%d日"
    
    I18N_SUBSITES = {
        'en':dict(
            LOCALE= u'zh_CN.UTF8',
            SITENAME= "SiteName"
        ),
    }
    JINJA_EXTENSIONS = ['jinja2.ext.i18n']


**注意**：locale需要与你系统一致（或支持），Ubuntu的locale可以在/etc/default/locale看到，不要问我win的locale是什么我也不知道= =

2、编译messages.mo文件

翻译文件message.po已经写好了，要让i18n识别这些文件需要编译出二进制的.mo文件来，在主题目录下输入以下命令：

    :::python
    pybabel compile --directory translations/ --domain messages


如果没有安装babel，则先执行

    :::python
    pip install babel


之后再

    :::make
    make html


就能完成主题的配置。看看你的博客是不是变漂亮了。

如果你修改了主题的模板（即templates的文件），需要重新生成`.po`文件，执行以下命令：

    :::python
    pybabel extract --mapping babel.cfg --output messages.pot ./
    pybabel update --input-file messages.pot --output-dir translations/ --domain messages
    pybabel compile --directory translations/ --domain messages


之后的就和上面一样了。

3、其他事项

如果你想完全使用farseerfc的主题，需要搭配一些插件:

    :::python
    PLUGINS = ["i18n_subsites",
               "plantuml",
               "youku",
               "youtube",
               'tipue_search',
               'neighbors',
               'series',
               'bootstrapify',
               'twitter_bootstrap_rst_directives',
               "render_math",
               'extract_toc',
               'sitemap',
               'gzip_cache',
               'summary']


部分插件需要beautifulsoup4支持，执行以下命令安装：

    :::python
    pip install beautifulsoup


由于farseerfc使用的是reStructuredText，如果你使用markdown，需要在pelicanconf.py添加：

    :::python
    MD_EXTENSIONS = ['admonition',
                     'toc',
                     'codehilite(css_class=highlight,linenums=False)',
                     'extra']


对于`.md`如果需要目录则添加`[TOC]`标签
* * *

###代码高亮

实现代码高亮用的是pygments和codehilite插件，按以下格式书写

\```

:::python

代码

\```

如果希望出现行号，并且效果像我的这样，则在目录`~/pelican-bootstrap3/static/css/style.css`添加修改以下代码（已有的部分不必重复）

```
:::css
.highlight pre {
    counter-reset: linecounter;
    padding-left: 1.5em;
    border-left: 3px solid !important;
    border-left-color: #FF8000 !important;
}
.highlight pre span.code-line {
    counter-increment: linecounter;
    padding-left: 1em;
    text-indent: -1em;
    display: inline-block;
}
.highlight pre span.code-line:before {
    content: counter(linecounter);
    padding-right: 1em;
    display: inline-block;
    color: grey;
    text-align: right;
    -webkit-user-select: none;
    -khtml-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
}
```

在`pelicanconf.py`相应位置添加修改以下项目

```
:::python
PLUGINS = ["better_codeblock_line_numbering"]
MD_EXTENSIONS = ['codehilite(css_class=highlight)']
```

* * *

###未尽事宜
[主题下载地址](https://github.com/farseerfc/pelican-bootstrap3)

如有其他疑问欢迎留言。
