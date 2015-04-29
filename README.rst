worldsim
========

.. image:: https://travis-ci.org/EllaBot/worldsim.svg

A world simulator, where the agent can be controlled with linear and angular velocities.

Physics
-------

Given the linear and angular velocities, the position of the agent is calculated as follows:

.. code::

    θ := (θ + ω * dx) mod π/2
    x := x + sin(θ + π/2) * v * dt
    y := y + cos(θ + π/2) * v * dt
