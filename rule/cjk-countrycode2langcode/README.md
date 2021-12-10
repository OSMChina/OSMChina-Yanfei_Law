# target
`name`,`brand`,`network`,`operator`,`description`

# mandatory
["name:jp"]->["name:ja"]
["name:cn"]->["name:zh"]
["name:kr"]->["name:ko"]

# optional
["name:ch"]->["name:zh"] //因为ch是查莫罗语，不建议自动化

# not
`krb`,`krc`,`krj`,`krl`,`kru` -x-> `ko`
`chl`,`chm`,`chn`,`chp`,`chr`,`chu`,`chy` -x-> `zh`

# note
对于`source`,`note`,`fixme`及其他少量出现，建议josm或者level0手动改
