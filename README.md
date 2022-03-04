<p align="center">
    <a href=#><img src="https://raw.githubusercontent.com/jbocane6/logos/main/holberton-logo.png" alt="holberton" /></a></p>


# 0x00. AirBnB clone - The console



  ## How to use

    ## Commands
    
        This console supports the folow commands:
    
        - create: create <class>
        - show: show <class> <id> or <class>.show(<id>)
        - destroy: destroy <class> <id> or <class>.destroy(<id>)
        - all: all or all <class> or <class>.all()
        - count: count <class> or <class>.count()
        - update: update <class> <id> <attribute name> "<attribute value>" or
        <class>.update(<id>, <attribute name>, <attribute value>) or <class>.update(<id>, <attribute dictionary>)

  - ### Interactive mode
    ```
    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) User.count()
    0 
    (hbnb) 
    (hbnb) quit
    $
    ```
  - ### No interactive mode:

    ```
    $ echo "help" | ./console.py
    (hbnb) 
    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) 
    $
    ```

  

# Performed by Carlos Matallana.