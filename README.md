[PyPi Package Page](https://pypi.org/project/JMaths/)

# Install
`pip install JMaths`
### System wide
`pip install JMaths --break-system-packages`

# JMaths
I created this library because I have a problem. I don't like the math animation libraries already out there. So I'm not making a math animation library but a library made for function analysis for excel.

### Note for self
Upload to PyPi
1. Update Package Version
2. `cd ~/Documents/JMaths/JMaths`
3. `python3 -m build`
4. Delete Old Files in /JMaths/JMaths/dist
5. `python3 -m twine upload dist/* --verbose`
6. `pip install JMaths==0.x.x --break-system-packages`