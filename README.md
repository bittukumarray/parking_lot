# parking_lot
I have made these assumptions:

- Driver can't be under 18, if any request comes up with driver age below 18, I am not storing this detail and one message will be shown that "driver should be on or above 18 years old".
- Registration number must be unique
- Input format must be correct
- If slots get full and one more request comes to give a parking slot, "no slots available message will be generated"
- While searching by registration_number, and driver's age, if no data found then I am not displaying any message, I am just printing a newline, since the same was done in the sample test case.
- In case of command "Vehicle_registration_number_for_driver_of_age", I am showing the registration numbers separated by comma.

