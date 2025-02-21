"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from cmath import nan
from math import isnan
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self.designation = info.get('pdes', None)
        self.name = info.get('name', None)
        self.diameter = info.get('diameter', float('nan'))
        self.hazardous = info.get('pha', False)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is None:
            return self.designation
        return f'{self.designation} ({self.name})'

    @property
    def _diameter_to_str(self):
        """Return a string 'unknow' or 'diameter of {value}'
            depending if neos has known diameter
        """
        if isnan(self.diameter):
            return "unknown diameter"
        return f"diameter of {self.diameter:.3f} km"

    @property
    def _hazardous_to_str(self):
        """ Returns a string "is" or "is not" depending
            on the potentially hazardous nature of neo
        """
        if self.hazardous:
            return "is"
        return "is not"


    def __str__(self):
        """Return `str(self)`."""
        if self.designation:
            return f"A NearEarthObject " + self.fullname + f" has a " + self._diameter_to_str + " and "+ self._hazardous_to_str +" potentially hazardous."
        return 'No matching NEOs exist in the database.'

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"

    def serialize(self):
        """ Return a serialize dictionary for output printing"""
        serialize_dict = {}

        serialize_dict['designation'] = self.designation
        serialize_dict['name'] = self.name
        serialize_dict['diameter_km'] = self.diameter
        serialize_dict['potentially_hazardous'] = self.hazardous

        return serialize_dict

class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = info.get('des', None)
        if (info.get('cd', None) is None):
            self.time = None
        else:
            self.time = cd_to_datetime(info.get('cd')) 
        self.distance = info.get('dict', float('nan'))
        self.velocity = info.get('v_rev', float('nan'))
        self.neo = info.get("neo", None)

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    @property
    def fullname(self):
        """ Returns the fullname of the NEOS object the class of CloseApproach pointing
            towards
        """
        return self.neo.fullname

    def __str__(self):
        """Return `str(self)`."""
        return f"On " + self.time_str + ", " + "'" + self.fullname +f"' approaches Earth " \
                  f"at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"

    def serialize(self):
        """ Return a serialize dictionary for output printing"""
        serialize_dict = {}
        if self.time is None:
            serialize_dict['datetime_utc'] = ''
        else:
            serialize_dict['datetime_utc'] = self.time_str
        serialize_dict['distance_au'] = self.distance
        serialize_dict['velocity_km_s'] = self.velocity

        return serialize_dict
