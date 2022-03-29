
#!/bin/bash

if [ ! -d "venv" ] 
then
	echo "The python environnement does not exist yet"
	python3 -m venv venv
fi
echo "The Python virtual envrionnement is now created"
echo "Activate"
source venv/bin/activate
echo " Load Dependencies "
pip install -r requirements.txt
echo "Done"
echo "------------------------------------------------------------------"
echo "The virtual environnement has been activated, running the code ..."
python main.py
echo "Process completed !"
pause
i
