<!DOCTYPE html>
<html>
<body>

<h1>Create a New Event</h1>

<h4> Event Name: <input type="text" name="eventName" value="<?php echo $eventName;?>"> </h4>

<h4> Location: <input type="text" name="eventLocation" value="<?php echo $eventLocation;?>"> </h4>

<h4> Start Date: <input type="date" name="eventStart" value="<?php echo $eventStart;?>"> </h4>

<h4> End Date: <input type="date" name="eventEnd" value="<?php echo $eventEnd;?>"> </h4>

<h4> Number of Timeslots: <input type="number" name="numTimeslots" value="<?php echo $numTimeslots;?>"> </h4>

<input type="button" name="submitButton" value="Submit">

</body>
</html>