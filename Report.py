def get_event_date(event):
  return event.date 

def current_user(events):
  events.sort(key=get_event_date)
  machines ={}
  for event in events:
    if event.machine not in machines:
      machines[event.machine]=set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    if event.type == "logout"and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine,users in machines.items():
    if len(users) > 0:
      user_list=",".join(users)
      print("{}: {}".format(machine,user_list))

class Event:
  def __init__(self,event_date,event_type,machine_name,user):
    self.date=event_date
    self.type=event_type
    self.machine=machine_name
    self.user=user

events = [ 
    Event('2020-01-21 12:40:54', 'login', 'web.local', 'Jay'),
    Event('2020-01-22 16:34:34', 'login', 'sql.local', 'nan'),
    Event('2020-01-21 13:45:12', 'logoin', 'dns.local', 'Annie'),
    Event('2020-01-22 17:21:23', 'login', 'web.local', 'Chris'),
    Event('2020-01-21 15:54:54', 'logout', 'dns.local', 'nan'),
    Event('2020-01-23 11:23:50', 'logout', 'mail.local', 'Annie')
]

users= current_user(events)
print(users)

generate_report(users)