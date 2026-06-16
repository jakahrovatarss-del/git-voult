---
type: daily
date: <% tp.file.title %>
---

# <% tp.file.title %>
>
>**Prev::** [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]]
>**Next::** [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]
>**Parent::** [[<% tp.date.now("YYYY-MM", 0, tp.file.title, "YYYY-MM-DD") %>]], [[<% tp.date.now("YYYY-[W]ww", 0, tp.file.title, "YYYY-MM-DD")  %>]]
>
> ---
> - [google calendar link](www.googlecalendar.com)
> - [tracking app]()


> [! sun]- ## Good morning. Now say it back.
> ### 📋 Log Morning
> log-sleep-hours:: 0
> log-sleep-rating:: 0
> log-wake-up-time:: 
> 
> log-morning:: 
> 
> ### ✅ Things to get done today:
> - [ ] Call me mum
>
> ### ☑ Extra things if I feel like it
> - [ ] PRIPRAVA NA MATURO
> 
> ### 🗓 Schedule
> - ŠOLA


> [! sun]- ## KUAS DELU U SOL
> ### 📋 Log ŠOLA
> log-URE:: 
> log-ZANIMIVOST:: 
> log-TEŽAVNOST:: 
> 
> log-KUA SI ELU PO ŠOLI:: 
> 
> ### ✅ Things to get done today:
> - [ ] PROBI SE NE FENTAT⏫ 
>
> ### ☑ Extra things if I feel like it
> - [ ] PRIPRAVA NA MATURO
> 
> ### 🗓 Schedule
> - ŠOLA
> - 


> [! sun]- ## VIKEN-POČITNCE
> ### 📋 Log KUAS DELU
> log-URE:: 
> log-ZANIMIVOST:: 
> log-TEŽAVNOST:: 
> 
> log-LJUDJE
> 
> ### ✅ Things to get done today:
> - [ ] PROBI SE NE FENTAT⏫ 
>
> ### ☑ Extra things if I feel like it
> - [ ] PRIPRAVA NA MATURO
> 
> ### 🗓 Schedule
> - MEJ SE FAJN PA SE UČ
> - 



















> [! moon]- ## Evening Review
> - log-day-review:: The day that I made history by licking a wet candle fire.
> - log-day-rating:: 0
> 
>> ### 🎵  Songs of the day
>> - log-song-of-the-day:: 
>
>> ### 📂 Which files we created this day
>> ``` dataview
>> list
>> where file.cday = date(<% tp.file.title %>)
>> sort file.ctime desc
>
>> ### 🗃 Which files were modified last this day
>> ``` dataview
>> list
>> where file.mday = date(<% tp.file.title %>)
>> sort file.ctime desc

