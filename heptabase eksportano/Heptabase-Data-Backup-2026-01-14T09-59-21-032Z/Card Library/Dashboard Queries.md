# Dashboard Queries

# Upcoming lectures

```dataview
table without id file.link as Lecture, Module, file.day - date("today") as "Days"
from "Sources/Lectures"
where file.day > date("today")
```

# Review lectures

```dataview
table without id file.link as Lecture, Module, date
from "Sources/Lectures"
where file.day < date("today")
```

# Active Modules

```dataview
table without id file.link as Modules, Assessments
from "Research/Modules"
where Active
```

# Other Modules

```dataview
table without id file.link as Modules, Assessments
from "Research/Modules"
where !Active
```

# Upcoming Assessments

```dataview
table without id file.link as Assessment, Module, Date, Deadline
from "Research/Assessments"
where date >= date("today") and date <= date("today") + dur("7 days")
sort date asc
```

# Other Assessments

```dataview
table without id file.link as Assessment, Module, Date, Deadline
from "Research/Assessments"
where date > date("today") + dur(7 days)
```

```dataview
table without id file.link as "No Date", Module, Date, Deadline
from "Research/Assessments"
where !date
```

# Sources

```dataview
table without id file.link as Sources, file.ctime as "Created"
from "Sources/Content"
sort file.ctime desc
```

# Tasks

```dataview
task
group by file.link
```