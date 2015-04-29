worldsim
========

A world simulator, where the agent can be controlled with linear and angular velocities.

Physics
-------

Given the linear and angular velocities, the position of the agent is calculated as follows:

.. math::
    \theta \leftarrow (\theta + \omega dx) \mod \frac{\pi}{2}
    x \leftarrow x + \sin(\theta + \frac{\pi}{2}) \times vdt
    y \leftarrow y + \cos(\theta + \frac{\pi}{2}) \times vdt
