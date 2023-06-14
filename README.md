# XPlanePythonAPI

Python library for getting and manipulating X-Plane values via UDP.

## How to use

### Initialize

```python
from xplane_api import XPlaneUdp
xp = XPlaneUdp()
```

### Read Data

```python
xp.AddDataRef("sim/flightmodel/position/indicated_airspeed", freq=1)
xp.AddDataRef("sim/flightmodel/position/latitude")

values = xp.GetValues()
print(values)
```

### Write Data

```python
xp.WriteDataRef("sim/flightmodel/position/latitude", 35.200, vtype='float')
```

### Send Command

```python
xp.WriteCommand("sim/lights/beacon_lights_on")
```

## DataRef and Command

You can find DataRef name and command name at below files.

- DataRefs.txt
- Commands.txt

These files are located in `{XPlane-Directory}/Resources/plugins` folder.
If you use addon airplane, please check `{XPlane-Directory}/Aircraft/{Addon-plane}` folder.

## References

[XPlaneUDP](https://github.com/charlylima/XPlaneUDP) by [charlylima](https://github.com/charlylima)
