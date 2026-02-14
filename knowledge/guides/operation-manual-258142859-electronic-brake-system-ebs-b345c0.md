---
category: transmission
created_at: '2026-02-12T01:05:57.879222'
doc_family: knowledge
source_type: guide
title: Operation Manual 258142859 Electronic Brake System EBS
truth_level: L3
updated_at: '2026-02-12T01:05:57.879287'
verification_status: unverified
---

Electronic Brake System EBS
Manual
Version 1.5 27/08/2025

Content
ii  /  lvi Manual_Electronic_Brake_System_EBS Bosch Motorsport
1 Warnings and Safety Instructions ................................................................................................................................. 3
2 Before Use ........................................................................................................................................................................ 4
2.1 Safety Information ............................................................................................................................................................................................... 4
2.2 Why Electronic Brake System EBS? ................................................................................................................................................................ 5
2.3 Principle of Operation ........................................................................................................................................................................................ 6
3 Technical Data ................................................................................................................................................................. 7
4 Adaptations to your Vehicle .......................................................................................................................................... 11
4.1 Transport of your Vehicle .................................................................................................................................................................................. 11
5 Assembling the Parts ...................................................................................................................................................... 12
5.1 Mounting Bracket ................................................................................................................................................................................................. 12
5.2 EBS Unit .................................................................................................................................................................................................................... 12
5.3 Brake Lines .............................................................................................................................................................................................................. 13
5.4 Suction Lines .......................................................................................................................................................................................................... 14
5.5 Brake Fluid ............................................................................................................................................................................................................... 15
6 Laptop Communication .................................................................................................................................................. 16
7 Programming and Diagnosis Software ......................................................................................................................... 17
7.1 Installing .................................................................................................................................................................................................................. 17
7.2 Features .................................................................................................................................................................................................................... 20
8 Startup Checklist ............................................................................................................................................................. 36
9 CAN Protocols ................................................................................................................................................................. 37
9.1 CAN Signal Description ...................................................................................................................................................................................... 37
10 Leakage Recognition ....................................................................................................................................................... 44
11 PWM Signal Description ................................................................................................................................................. 45
11.1 PWM Pins ................................................................................................................................................................................................................ 45
11.2 PWM Hardware Interface .................................................................................................................................................................................. 45
11.3 PWM Signal Interpretation ............................................................................................................................................................................... 45
12 Disposal ............................................................................................................................................................................ 46
13 Legal ................................................................................................................................................................................. 47
13.1 Legal Restrictions ................................................................................................................................................................................................. 47
14 3D Models ........................................................................................................................................................................ 48
15 Offer Drawings ................................................................................................................................................................ 49
15.1 Offer Drawing EBS Unit ...................................................................................................................................................................................... 49
15.2 Offer Drawing Mounting Board ...................................................................................................................................................................... 50
15.3 Offer Drawing Pressure Sensor ....................................................................................................................................................................... 51
15.4 Wiring Diagram ..................................................................................................................................................................................................... 52
15.5 Wiring Harness ...................................................................................................................................................................................................... 53

Warnings and Safety Instructions | 1
Bosch Motorsport Manual_Electronic_Brake_System_EBS 3  /  56
1 Warnings and Safety Instructions
The classification of the warnings and safety instructions is carried out by the respective
signal word (Danger, Warning, Caution) next to the warning symbol.
Danger
Nature and source of danger
Consequences
Warning of death or serious physical injury, which are sure to occur if ignored.
Warning
Warning of death or serious injury, which can occur if this is not observed.
Caution
Warning of slight bodily injury in case of Disregard.
Notice
Warning of damage to equipment in case of ignoring.

2 | Before Use
4  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Read these instructions carefully and follow the recommendations for use step by step.
We are happy to give you additional notes and explanations. Our contact information is
on the back cover of this manual.
2.1 Safety Information
The EBS Kit was developed for use by professionals and requires in-depth knowledge of
automobile technology and experience in motorsport. Using the system does not come
without its risks.
It is the duty of the customer to use the system for motor racing purposes only and not
on public roads. We accept no responsibility for the reliability of the system on public
roads. If the system is used on public roads, we shall not be held responsible or liable for
damages.
The EBS system is not active in standstill. Use EBS Diagnosis Software (RaceABS) for dia-
gnostics.
We recommend working on the system with power off and EBS system depressurized.
Depressurize the EBS System of your vehicle before transporting it
by airplane.
With EBS Diagnosis Software (RaceABS), you can depressurize the EBS system in a few
moments. Reactivate the system before the next use.
It is essential that the predefined Bosch Motorsport assembly guidelines are complied
with the system to run properly, see section Assembling the Parts [ }   12 ] . This applies
above all for installing the MIL (malfunction indication lamp) within the driver's range of
visibility.
Safety concept
Two pressure sensors (one internal, one PWM input) to monitor the system pressure en-
sure high safety standard. Due to system monitoring, the risk of unintended braking is
significantly reduced.
If the pump motor fails, a warning is set and the EBS-system is able to perform the next
following driver brake request due to the 160 bar pre-filled reservoir.
If there is an EBS failure during the race, a backup mode automatically takes effect. From
this moment on, only hydraulic braking takes place. This enables the driver to brake reli-
ably at all times.

Before Use | 2
Bosch Motorsport Manual_Electronic_Brake_System_EBS 5  /  56
2.2 Why Electronic Brake System EBS?
Features:
– Braking system for one axle
– Supplement to the hydraulic brake
– Braking energy is recovered (recuperation)
– Recuperation share should always be maximum
– The hydraulic brake takes over individual wheel decelerations
– In case of system failure the hydraulic brake takes over
To maximize the efficiency of electric or hybrid vehicles, the electro motor shall recuperate
the maximum possible amount of energy while braking. The brake torque from the electro
motor varies over speed. Therefore, the hydraulic brake torque at the electrically driven
axle must be controlled “by wire” to compensate the varying brake torque from the elec-
tro motor.
The aim of the system is to keep the brake balance between the front and rear axle con-
stant.

6  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
2.3 Principle of Operation
Bosch Motorsport EBS is suitable for one axle actuation . It is based on a series produc-
tion type and adapted in years of development work to meet motorsport requirements.
The EBS is controlling the hydraulic pressure in one axle according to the recuperation
values. The EBS has a 160 bar pressurized reservoir. By applying the brake pedal, a valve
will cut the connection between the pedal and the calipers.
Simultaneously the VCU will calculate the regeneration level and extract from the driver
brake request the amount of electrical part. The remaining amount will be generated by
EBS as hydraulic pressure using the 160 bar prefilled accumulator. By releasing the brake
pedal, the brake fluid from caliper will be fed into the Master Cylinder MC reservoir.
Three types of EBS
In general, we distinguish between three types of EBS systems:
– Type 1 gets pressure target from external software (used in LMDh).
– Type 2 gets torque target from external software.
– Type 3 works with EBS internal calculations and sends requirements to the electrical
motor. This project will be finished only on customer request.
Six different braking characteristics
As an example, we designed six different characteristic profiles for the EBS system to en-
able different actuation strategies. With a six-steps-switch, you can choose between these
profiles, e.g., from
1. very soft EBS controller activity to
2.
3.
4.
5.
6. maximum EBS controller activity.

Technical Data | 3
Bosch Motorsport Manual_Electronic_Brake_System_EBS 7  /  56
3 Technical Data
Mechanical Data
Hydraulic unit
Serial housing, dust- and damp-proof
Vibration damped circuit board
38 pin connector
6 hydraulic valves for inlet/outlet
1 separation backup valve
1 electric pump motor
1 hydraulic accumulator 160 bar/90 cm
Standard fittings M12 x 1
Size 176 x 144 x 157 mm
Operating temperature -30 to 130°C
Max. shock 50 g less than 6 ms
Max. working pressure 130 bar; max. recommended locking pres-
sure 120 bar
Max. pressure gradient up to 2,000 bar/s
Pressure Medium
DOT 4 brake fluid
DOT 5.1 brake fluid
Electrical Data
Supply voltage 10 to 16 V
max. 24 V for 5 min
Max. peak voltage 35 V for 200 ms
Max. peak at start <165 A
Current consumption Pump <40 A
Current consumption Relay <16.5 A
Power consumption Electronics <1.5 A
Inputs
1 x PWM Target (Pressure or Torque)
1 x PWM input calliper pressure
1 x CAN1; 500 k or 1 Mb selectable
1 x CAN1 DC (Daisy Chain)
EBS function switch 6 positions via CAN1
Outputs
EBS warning light (MIL) via CAN1
EBS diagnostic via CAN1

8  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Required Additionals
Mounting Board for Hydraulic Unit
Pressure Sensors Fluid PSS-260 2 required
Com Interface MSA Box II Required for communication and program-
ming, not mandatory if available
Spare Parts
Mounting Rubber Elements Kit 5 sets (10 units Ø 18 mm;
5 units Ø 23 mm)
Component Weights
Hydraulic Unit 3,630 g
Mounting Board for Hydraulic Unit 300 g
2 Pressure Sensors Fluid PSS-260 40 g/each
Vehicle specific wiring harness with
motorsport connectors
Depends on version
Connectors
Connector EBS Unit 38-1 EuCon F02U.B00.238-01
Connector Pressure Sensor D261.205.335-01
Connector Diagnosis F02U.000.258-01
Connector 38-1 EuCon

37
26
27
28
29
30
31
32
33
34
35
36
18
15
16
17
14
19
20
21
22
23
24
6
7
8
9
10
11
12
1 25
38 13

Bosch Motorsport Manual_Electronic_Brake_System_EBS 9  /  56
Pin Configuration
1 UB_MR
...
13 GND_MR
14 CAN1M
15 CAN1M-DC
...
25 UB_VR
26 CAN1P
27 CAN1P-DC
28 WAU_IN
...
31 PWM Gnd
...
33 PWM 5 V
...
36 P_Target_PWM
37 P Caliper PWM in
38 GND_ECU

10  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Daisy Chain
Please note that inside the ECU CAN and daisy chain CAN are linked.
Signal Name: CAN1M Pin Number: 14
Signal Name: CAN1M-DC Pin Number: 15
Signal Name: CAN1P Pin Number: 26
Signal Name: CAN1P-DC Pin Number: 27
Schematic (vehicle side) Interface circuit (ECU side)

CANM
CANP
CANP_DC
CANM_DC

System ASIC
5V
+
-
VCAN_L
VCAN_H
Item Min Typ Max Unit
Reference GND_ECU
Bit rate 500 k bit/s
Differential Input voltage (Dominant)
VCAN_H - VCAN_L, UinDifDom
0.9
Differential Input voltage (Recessive)
VCAN_H - VCAN_L, UinDifRec
0.5
Differential Output voltage (Dominant)
VCAN_H - VCAN_L, UoutDifDom
1.5 3.0
Differential Output voltage (Recessive)
VCAN_H - VCAN_L, UoutDifRec
-0.5 0.05
Input resistance, Rin 11.25 k 22.5 k 33.75 k Ohm
Output bus voltage (Dominant)
VCAN_H, U_CANP_dom
2.75 3.5 4.5 V
VCAN_L, U_CANM_dom
0.5 1.5 2.25 V
Output bus voltage (Recessive)
VCAN_H, U_CANP_rec
2.0 2.5 3.0 V
VCAN_L, U_CANM_rec

Adaptations to your Vehicle | 4
Bosch Motorsport Manual_Electronic_Brake_System_EBS 11  /  56
4 Adaptations to your Vehicle
Physical vehicle data
For optimum brake performance, each EBS unit has to be customized to suit the vehicle in
which it is to be used.
Wiring harness
A wiring harness can be provided.
Do not connect ABS M4 or M5 loom to EBS .
This would destroy the EBS module.
Electrical requirements
The EBS needs to be networked electrically to the VCU .
The EBS does not have a separate MIL. The MIL function is sent to the driver display via
CAN. In the driver's display this CAN signal must be translated into a message to the
driver indicating the absence of the CAN signal.
You need a DBC file to run the EBS.
Please ensure that the system is in Force Passive mode during the
boot phase.
Hydraulical requirements
All hydraulic connections between EBS, master brake cylinder, pedal feel modulator and
axle must meet a brake-specific standard.
The suction line of the EBS needs to be connected hydraulically to the main brake pres-
sure fluid reservoir of the main cylinder. The use of two separate reservoirs could lead to
them taking each other's volume.
4.1 Transport of your Vehicle

5 | Assembling the Parts
12  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
5.1 Mounting Bracket
Avoid the mounting in an area where vibration can damage the master cylinder. Flexible
lines can avoid defects, if master cylinder and EBS are mounted very close together. Fit
rubber pads between the assembly plate and the vehicle chassis to reduce vibration.
Maintain a 10 mm distance between the vehicle chassis and the bottom of the assembly
plate to allow easy connection of the EBS electrical connector.
5.2 EBS Unit
1 2 3
No Shortcut Description Synonymous
1 SPC Sense Piston Connection Connection to Master Cylinder
2 PFC Pedal Feel Connection Pedal Simulation Connection
3 BPC Boost Piston Connection Caliper
4 RSV Reservoir Brake Fluid Reservoir

Assembling the Parts | 5
Bosch Motorsport Manual_Electronic_Brake_System_EBS 13  /  56
When installing EBS unit, make sure the Sense Piston Connection and the Pedal Feel Con-
nection are facing upwards to ensure air can be bled out.
The EBS unit is prefilled with brake fluid. During assembly, make
sure as little brake fluid as possible is lost.
When the hydraulic unit is delivered, it is pressure less and the pump is locked by soft-
ware. After installation, both the pump and the rest of the brake system must be bled, see
also chapter Repair Bleeding Wizard. Unlock the pump at the right moment by diagnostic
command.
The system is not ready for use when delivered!
Bleed and unlock the system before first use.
Now the pump can build up its operating pressure of 160 bar and is ready for operation.
For more on assembly see Offer Drawing EBS Unit [ }   49 ] .
We recommend an exchange of the EBS Unit after one year.
In racing vehicles, hydraulic units are subjected to significantly higher loads than in pro-
duction vehicles. We therefore recommend replacing them even when they are fully func-
tional, to keep the residual risk of failure as low as possible.
5.3 Brake Lines
Use rigid steel brake lines for as much of the plumbing as possible. Flexible lines should
be kept to an absolute minimum for optimal brake control and pedal feel.
The EBS units use a DIN (bubble) flare convention common to European OEM applica-
tions. For sizes, also see Offer Drawing Hydraulic Unit.
115°±2°
Tool marks
acceptable
Radius required,
no nicks allowed
øA
øB øA > øB

14  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
The EBS unit is secured in the vehicle on the provided mounting plate. During operation,
the EBS unit will vibrate. These vibrations are then transferred to the brake lines. To pre-
vent vibration-induced damage to the brake lines, they must not be secured at a distance
of up to 20 cm from the hydraulic unit so that they can vibrate freely.
We recommend using rigid metal brake lines; use flexible lines only
at points where they are necessary.
Do not secure brake lines 0 to 20 cm from the hydraulic unit. The
unit vibrates and would cause risk of damage to the lines.
Use brake lines with a minimum inside diameter of 3.3 mm.
5.4 Suction Lines
At EBS
Brake lines with an outer diameter of 4.7 mm (inner diameter 3.3 mm) are not sufficient
for an optimized pressure build up dynamic for the EBS . For a good pressure build up dy-
namic over the complete temperature range, Bosch recommends the use of 8 mm (outer
diameter) brake lines.
In general, it is recommended to install the hydraulic unit (HU) as near as possible to the
master cylinder (MC) to minimize the length for the suction line and the pressure drop. If
this is not possible, one of the following variants of the brake lines should be used.
– Suction line length < 1.0 m
– Prevent a suction line > 1.0 m, because the pressure drop and the function pres-
sure build up dynamic is restricted by a longer brake line.
– If it is impossible to install the hydraulic unit near to the master cylinder, an ex-
ception should be checked together with Bosch, additional pressure build up
measurements are necessary.
Fittings
Do not use anything else but the standard M12 fittings.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 15  /  56
5.5 Brake Fluid
Safety relevant due to influence on tightness of system to the outside and threat to
life and physical condition
The accumulator must be capable of utilizing any of the following glycol or glycol-ether
based brake fluids listed below (defined in SAE J1703, FMVSS 116 and ISO 4925 (JIS
K2233)) including a mix of any of the fluids in any combination.
– DOT3
– DOT4
– DOT4+(plus)
– DOT4NV
– DOT5.1
– SuperDOT4+(plus)
– As the accumulator is to be used in a braking system, it is necessary that the accumu-
lator does not contain chlorine- or sulphur-containing inorganic substances or free
copper, as this can lead to critical corrosion in the hydraulic unit, with the risk of in-
ternal/external leakage or loosening of HU components under high pressure (-
>highest severity). As well, it must also not contain mineral oil nor plasticizers/soften-
ers on phthalate basis (including components that may segregate these substances).
Contamination with mineral oil can result in a breakdown of the
brake system!

6 | Laptop Communication
16  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
The MSA-Box II from Bosch Motorsport is the communication interface between EBS and
the programming and diagnostic software on your laptop. The MSA-Box II has two con-
nectors: a USB connector for connection to the laptop and a motor sports connector for
connection to the mating connector in the vehicle wiring harness.
Installing the MSA-Box II driver:
Before using the MSA-Box II for the first time, you need to install a specific driver on your
laptop. Find the driver for free download on our website www.bosch-motorsport.com.
Please make sure that the MSA-Box II is not connected to the laptop
while you are installing the driver.
Connect the MSA-Box II to the laptop after installing the driver. This will trigger the initial
communication between the laptop and the MSA-Box II. Follow any prompts that may fol-
low to install the MSA-Box II. Once you complete any prompts and computer recognizes
the MSA-Box II, the MSA-Box II is ready for use.
Steps:
1. Unplug the MSA-Box II from the laptop.
2. Install the driver.
3. Plug the MSA-Box II into the laptop.
You can connect EBS to a laptop with the MSA-Box II via the "diagnosis interface" con-
nector. The diagnosis interface connector should be placed so it is easily accessible. You
can use programming and diagnosis software, see section Programming and Diagnosis
Software, to program settings specific to the vehicle and open/delete error messages.

Programming and Diagnosis Software | 7
Bosch Motorsport Manual_Electronic_Brake_System_EBS 17  /  56
7 Programming and Diagnosis Software
7.1 Installing
After installing the MSA-Box II, you need to install the programming and diagnostic soft-
ware RaceABS. You can find the software for free download on our website: www.bosch-
motorsport.com
Switch on the ignition
Plug the MSA-Box's USB connector into your laptop and its motorsport connector into the
EBS wire harness diagnostic interface to enable communication.
The installation creates a shortcut on your desktop to the RaceABS software. Click it to
start the application. A green status indicator shows when the connection is successful. A
window pops up where you can select your brake system, choose EBS in this case.
Next step is to choose the CAN Baud Rate of your EBS system. It is the same CAN Baud
Rate as your ECU: 500 kB or 1 MB .
Click OK and the main window opens.
Behind the orange button in the left corner of the headline, you will find information
about your RaceABS version, license terms and OSS details.

18  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
If you try to launch the software without the MSA-Box II to laptop connection, the status
indicator in Explorer lights red / yellow and an error message appears in the status bar:
Colors of the status indicator
The status indicator can light up in the following colors:
Red No connection
Yellow Connection in progress
or
MSA-Box II cannot create a connection with the EBS (e.g.
EBS switched off)
Green Connection successful, Online mode
White Offline mode
Red / Yellow flashing MSA-Box II is not connected to the laptop

Bosch Motorsport Manual_Electronic_Brake_System_EBS 19  /  56
Change between Online and Offline Mode
If a connection does not exist, it is easier to operate with the diagnosis software in Offline
Mode. Please click with the right mouse button on the status indicator to choose between
Online and Offline Mode:
Custom Theme Selection
Selection of Custom Themes / Skin is now possible in RaceABS. This helps the customer to
configure the Tool as per his requirements.

20  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
7.2 Features
Diagnostic Code
The EBS -ECU sends the stored errors as coded data to RaceABS. These codes are then
translated by a translation file and displayed on the page “Ecu Info” in RaceABS as plain
text.
After installation of RaceABS, a default file will be used for the translation. If you don´t see
plain text or if there is an orange colored warning, you do not have the matching transla-
tion file to your software. With a not matching file, some codes cannot be translated or
might be translated in the wrong way. Therefore it is important to use the correct transla-
tion file.
To get the correct translation file, please conduct the following steps:
– Check on the top of the “ECU Info” page which software number and software version
is used in your EBS .
– Go to the Bosch Motorsport homepage and download the matching diagnostic trans-
lation file to your software. You will find in the naming of the diagnostic translation
file the software number as BB number and the version as a V number, zeros at the
end might be skipped in the naming. The numbers of the file need to match the num-
bers of the software. The file is an .XML file.
– For example if your EBS runs on the Software Number 99703 and the Software
Version 03.00.07.01.00.00, you will need the Diagnostic errors file (99703/
v03.00.07.01.00.00).
– Store the file on your computer.
– Click in RaceABS on “Properties” - “Diagnostic Errors” and select the matching diag-
nostic translation file.
You will find the most common translation files on our homepage. If your needed file is
missing, please contact your dealer or the OEM customer service.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 21  /  56
7.2.1 Vehicle Data
Fill in the weight of your vehicle in kg at ENV_mVehicle .
The parameters in the Brake area in the right part of the window are pre-filled by Bosch
Motorsport and can only be changed after consultation with us.
– P_Cp_Axle shows the friction value between brake pad and disc.
– PWM_Target_Minimal_Request shows in percentage the minimum triggering limit.
Beneath this value, no PWM target will be implemented. The value should be a little
higher than the toggle value. You will get the toggle value by analyzing the EBS data.
7.2.2 ECU Info (Diagnostics)
If you connect your vehicle with your laptop via MSA box, the EBS will fill in the values for
Software Number, Software Version, Ignition Cycle Counter, App Name and Build Data.
Indication lamp
When you turn on the ignition or the EBS , the warning light (MIL) comes on briefly and
then turns off again. This indicates the light's self-testing process. If the warning light
(MIL) does NOT light up when you turn on the ignition or the EBS , you must establish the
reason for this before taking any further action or before driving the vehicle.
The MIL will stay illuminated as long as the diagnostic tool is
switched on.
If you use a wrong software version, the MIL will blink from the mo-
ment you are driving. It will not blink in standstill.
Error log
If the warning light (MIL) is illuminated PERMANENTLY when you turn on the ignition or
the EBS , or while driving, there is a system error. Extract the system's internal error log to
analyse the error. You can access the log by clicking on the ECU Info tab in the RaceABS
software.

22  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Old errors are grey, actual errors are highlighted in orange.
You’ll find a complete overview of error log entries in an Excel sheet on the EBS product
site at www.bosch-motorsport.com.
System reset after drive cycle faults.
Drive cycle faults, e.g. PWM faults, need an EBS -ECU reset (Power off - Power on) in the
proof of a good signal.
ECU soft reset
Quicker than an ECU reset is an ECU soft reset. You can run it with a right mouse click and
ECU soft reset. ECU soft reset deletes error logs.
Save Faults
If any error log entries occur which are not explicit translated, please contact your dealer
or the OEM customer service. Communication would be easier if you also send a copy of
your error log entries.
Click on the right button named “Save Faults” to get a copy of your saved error files.
Clear Faults
After carrying out the problem-solving actions, delete the entry from the error log by
clicking on the Clear Faults button. Then turn EBS off and on again. After you deactivated
the software, the indication lamp will no longer glow.
After Clear Faults and ECU soft reset , only the actual remaining faults will be displayed.
If the faults are not all clearly described or if there is no error de-
scription, please check if you used the correct XML-file or contact
Bosch Motorsport for update.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 23  /  56
Ignition Cycle Counter
The Ignition Cycle Counter shows how often you switched on the ignition. If you compare
the values of the Ignition Cycle Counter and ICC at Failure Occurrence, you can trace back
at what time the faults occurred. If both fields show the same values, it is an actual fault.
The values of Ignition Cycle Counter ICC and Power Cycle Counter PCC are identical.
7.2.3 Testing
Valve Activation
The specific valve activation functionalities are for advanced troubleshooting and should
only be used by Bosch specialists.
Pump
Lock Pump
This function deactivates the electrical pump. With a locked pump, you can check how
many brake cycles are possible in the case of a pump failure. You also use this function if
you want to decrease the hydraulic pressure of the EBS system to zero.
Unlock Pump
Press Unlock Pump to reactivate the pump and rise the system pressure to 160 bar.
Pump should run now until the system pressure reaches 160 bar and switch off then.
Hands off from the calipers during the calibration process.
The EBS will activate the brakes, and this can lead to injuries.
Calibration
Calibration in general is not necessary periodically. We recommend it after installing the
EBS system into the vehicle. Please contact us if you need help or if you have any ques-
tions.
Press PWM Offset Calibration to calibrate the values P_Calip_PWM and P_Target_PWM
to zero. Make sure the VCU is sending "0", then press the button and follow the step-by-
step procedure.

24  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
The pressure sensors P_Axle and P_Driver are system-internal factory calibrated sensors. If
the hands of the P_Axle- and the P_Driver-clocks are not facing to zero in stillstand, press
the P_Axle, P_Driver Calibration button and follow the step-by-step procedure.
If the values for BIVcX Offset and BOVcx Offset , displayed at the bottom of the Testing
page , are different from the respective standardCalibOffset values displayed in the
VehicleData page , you need to run the Valve Calibration Std routine. After running the
routine, please make a power cycle.
If you still have problems, please contact Bosch Motorsport.
Wizard Group
Repair Bleeding
With this button, you will be guided step by step through the bleed of the EBS unit. This
might be required if air got trapped in the accumulator of the EBS unit. It is recommended
to perform the EBS unit bleed after installation or if air got trapped in the brake lines and
might got caught in the EBS unit.
Click on the button “Start Wizard”, a new window will open and lead you step by step
through the instruction for bleeding the EBS unit. You will need three people to conduct
the instruction. See also Repair Bleeding Wizard [ }   26 ] .
Master Cylinder Volume Check
Check your logged data before you start this function.
Here you can check if the volume of the main break cylinder offers enough volume to run
the EBS system safely. Therefore, the system closes the valve to the pedal feel simulator
abruptly and opens the valve to the mechanical brake at the same time. Now the brake
pressure on the axis should have at least 50 % of the value measured before. If the brake
pressure on the axis is significantly lower, the volume of the master cylinder is too small
and should be changed against a bigger one.
This check can also be very helpful in the case of suspected leakage at the master cylinder.
To run the check, press the Master Cylinder Volume Check button and follow the step-
by-step procedure.
Please log the data of P_Mc and P_Caliper shortly after the backup change for later ana-
lysis.
Pedal Travel Simulator Check
This function can be used for running the purposes of the pedal travel way. What is the
drivers feeling of the break? Does it feel too hard or too soft? Best would be if the driver
would not realize the EBS systems work.
Press the button and follow the step-by-step procedure.
Release Accumulator Pressure Release to 0
This function depressurizes the system to zero. Use it to depressurize the system for a
longer time or if you have to open the hydraulic system e.g., for repairing. Please lock the
pump at first.
The hand in the P_Accumulator clock should point to zero. Repeat if you have rests of
pressure in the system.
Please realize that the system was designed for a maximum number of 900 high pressure/
low pressure cycles.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 25  /  56
Actuator Test
This function checks the proper work of the valves. Please contact Bosch Motorsport for
using this function.
Brake Inlet Valve Leakage Test
Use this function if you have the suspicion of a leakage. Click the button and follow the
step-by-step procedure.
Piping Check
After assembling the pipes, you should check if all parts like pedal feel simulator, caliper
or reservoir are fitted correctly. Therefore, click the button and follow the step-by-step
procedure.
Sensors
P_Axle ( internal sensor inside the EBS unit) shows the hydraulic pressure of the mechan-
ical brake at the axle, see also graphic below.
P_Driver ( internal sensor inside the EBS unit) shows the drivers pressure on the brake
pedal.
P_Accumulator ( internal sensor inside the EBS unit) shows the pressure of the hydraulic
accumulator of the EBS, see also graphic below.
P_Mc_CAN (external sensor) shows the hydraulic pressure at the master cylinder. It is
measured by the VCU and is transmitted to the EBS via CAN.P_Driver andP_Mc_CAN
should be identical. See also graphic below.
P_Calip_PWM (external sensor) measures the pressure between the calipers and the EBS
and communicates with ECU and EBS system via CAN and PWM.
Targets
The EBS system gets the target values from an external software. They are handed over as
a torque value M or a pressure value P.
vVeh (m/s)
The vehicle speed vVeh should be zero in standstill.
Switch Position
Here you see the chosen switch position 1 to 6.

26  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
vVeh Qualifier
Quality information of the vVeh signal, as received via CAN.
Standstill
EBS recognized standstill when the vVeh is close to 0 m/s and the quality is valid.
ForcePassive
Indicates if the VCU is sending the "Force Passive" request on CAN
Bxxx Offsets
Show internal offsets for the different actuation valves. Used by Bosch specialists.
7.2.4 Repair Bleeding Wizard
This chapter describes the procedure of bleeding the hydraulic unit of the EBS system in
13 steps:
1. Unit preparation for bleeding
2. Bleeding MC to Caliper left without pedal pressure.
3. Bleeding MC to Caliper right without pedal pressure.
4. Bleeding MC to Caliper right/left with pedal pressure.
5. Bleeding MC to Pedal feel simulator without pedal pressure.
6. Bleeding MC to Pedal feel simulator with pedal pressure.
7. Close Bleeder Screw for pedal feel simulator
8. Bleeding Accumulator to Caliper left or right line without pedal pressure.
9. Close Caliper Bleeder Screw
10. Remove the 2 Bars from Reservoir
11. Bleeding Accumulator to Reservoir suction line
12. Recharge Accumulator with valves actuation
13. Bleeding Pressure release valves to Reservoir

Bosch Motorsport Manual_Electronic_Brake_System_EBS 27  /  56
Step 1: Unit preparation for bleeding
This step is preparing the system for bleeding.

28  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Step 2: Bleeding MC to Caliper left without pedal pressure
Bleeding the line between Master Cylinder and Caliper left. System is in passive mode, no
valves actuation. By using the 2 bar on the reservoir, the fluid will be pushed to Caliper.
Step 3: Bleeding MC to Caliper right without pedal pressure
Bleeding the line between Master Cylinder and Caliper right. System is in passive mode,
no valves actuation. By using the 2 bar on the reservoir, the fluid will be pushed to Caliper.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 29  /  56
Step 4: Bleeding MC to Caliper right/left with pedal pressure
Bleeding the line between Master Cylinder and Caliper right and left under pedal pressure.
System is in passive mode, no valves actuation. The pedal pressure pushes the air towards
the brake Caliper.
Note that by using balance bar you need to open front and rear bleeding screws simul-
taneously.
Step 5: Bleeding MC to Pedal feel simulator without pedal pressure
Bleeding the unit and pipe to pedal feel simulator. The fluid will start leaking after you
pressed Next button.

30  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Step 6: Bleeding MC to Pedal feel simulator with pedal pressure
Bleeding the unit and pipe to pedal feel simulator with pedal pump. The fluid will start to
leak after you pressed Next button.
When Step 6 is finished, close the Bleeder Screw.
If step 5 and 6 are not correct, air will be the reason for a long pedal in active mode.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 31  /  56
Step 7: Close Bleeder Screw for pedal feel simulator
If not done after step 6, close Bleeder Screw for pedal feel simulator.
Step 8: Bleeding Accumulator to Caliper left or right line without pedal pressure
System will start an active pressure increase after pressing the Next button.
In this step, it does not matter whether you use the Bleeder Screw 3 on the right Caliper
or the Bleeder Screw 3 on the left Caliper for bleeding. Both works equally well. We re-
commend using the Bleeder Screw that is more accessible.

32  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Step 9: Close Bleeder Screw 3 at the Caliper
Step 10: Remove the 2 bar from Reservoir
Reservoir needs to be opened to be able to collect the brake fluid volume from the pres-
sure release in step 11.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 33  /  56
Step 11: Bleeding Accumulator to Reservoir suction line
Pressure release will start after pressing the Next button.
Step 12: Recharge Accumulator with valves actuation
2 bar of pressure on the reservoir is optional. It is important that the reservoir is filled with
enough brake fluid.
After pressing Next button, the system will start a pressure increase with valves control.

34  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Step 13: Bleeding Pressure release valves to Reservoir
This is a verification step.
Press the pedal in normal frequency, but with full stroke. Pressure needs to drop by re-
leasing the pedal below 3 bar.
Action will start after pressing the Next button.
Pressing Finish will close the bleeding session.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 35  /  56
7.2.5 Function Switch
Configuration
CanBaudrateSwitch
Choose 500 kB or 1 MB for the communication of the EBS with the other devices inside
the car.
EBSType
Choose the type of your EBS system
– Type 1 gets target pressure from external software.
– Type 2 gets target torque from external software.
MCU CAN Monitoring
Deactivate specific monitorings in case the Bosch electric motor is not used.
Multiswitch
Default Position
For the function switch, you can specify a default value. If the switch fails for any reason, it
automatically takes the position of the default value. To assign a position for the default
value, select a number between 1 and 6 under “MultiSwitch” in the field “Default Position”.
When making your choice, take into account the information on the characteristics in
chapter Principle of Operation [ }   6 ] .
PWM Offset Calibration
The PWM Duty Offset values shown here are the results of the PWM Offset Calibration
you have previously performed in the Testing window, see also Testing [ }   23 ] . The values
can only be manipulated after consultation with Bosch Motorsport.

8 | Startup Checklist
36  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
This short checklist is intended to supplement the EBS ’s manual, not replace it. Prior to us-
ing this checklist, the user/installer should read the EBS manual, especially section Laptop
Communication to Assembling the Parts.
Basics
– EBS unit mounted as specified in the drawing Offer Drawing EBS Unit [ }   49 ] .
– Brake pressure sensor installed in proper location? See section Brake Pressure Sensor.
– Everything plugged in to harness, power ring terminals connected to battery, ground
ring terminals connected to solid and clean chassis ground, circuit breakers installed
properly, map switch turns off system. See section Brake Pressure Sensor.
Software Tool and Error Checking
– Connect to the EBS unit with MSA-Box II using RaceABS Software and ensure that all
vehicle data has been entered correctly. The vehicle data can be saved and or loaded
by right clicking in the screen.
– With the system on, switch to the “ECU Info” page and clear errors with clicking on
Clear faults. Wait a moment (system will self-refresh error stack). Reset the system by
switching off/on. Check if any errors reappear in the error stack. If errors reappear,
diagnose errors before proceeding. If anything was unplugged during the diagnostic
process, errors will be present and need to be removed from the error stack. Next,
verify no errors are present after cycling power, see section ECU Info (Diagnostics).
Error Notes
– Critical failures (like CAN or PWM), or the ForcePassive request, will prevent the pump
from running.
Function Check
– While connected with the RaceABS software, switch to the “Testing” page. Check all
sensors for plausibility and proper function. Rotate map switch, the value Switch Pos-
ition should turn up clockwise.
If the pump does not start, make sure that there is neither an error
message nor a Force Passive request.
"Force Passive request" means a request from the VCU to the EBS not to switch to the act-
ive state under any circumstances, refer to CAN DBC.

CAN Protocols | 9
Bosch Motorsport Manual_Electronic_Brake_System_EBS 37  /  56
9 CAN Protocols
The following tables give a short summary of the CAN protocol. If you need any details,
Bosch Motorsport will send you the latest .dbc version. Please send an email to
motorsport@bosch.com
The message EBS_Mes1 (0x3FF) only contains data for application and debugging. The
VCU / TorqueMaster does not need to read this message.
If you need more information on the CAN interfaces for the variant 2 or 3 of the EBS
(torque controlled, or EBS as brake torque master), please send an email to
9.1 CAN Signal Description
9.1.1 CAN Input Signal Information
EBSin_p_BrakeTarget
The requested target pressure that the EBS should set at the axle. This value should always
match the value transmitted on the PWM channel
EBSin_ForcePassive
Force the EBS to switch to passive mode. The connection from the master cylinder to the
brake caliper will be open. The target pressure request will be ignored.
EBSin_p_MC
The pressure measured between the master cylinder and the EBS, by an external sensor.
The EBS compares this value to its internal value to ensure the functional safety of the sys-
tem.
EBSin_p_MC_Quality
Quality information on the pressure measured by the external sensor. Refer to the exten-
ded qualifier values description below.
EBSin_Chassis_BrakePedalApplied
The state of the brake pedal measured by an external sensor. The EBS uses this value to
ensure the functional safety of the system.

38  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
EBSin_Chassis_BrakePedal_Quality
Quality information on the brake pedal state. Refer to the extended qualifier values de-
scription below.
EBSin_Chassis_vVeh
The current speed of the vehicle. This information is used to detect when the vehicle is
standing still. The EBS switch to passive mode (status Prerun) when the vehicle is in stand-
still. The Diagnostic communication with RaceABS is also only available when the vehicle is
EBSin_Chassis_vVeh_Quality
Quality information on the vehicle speed. Refer to the extended qualifier values descrip-
tion below.
EBSin_Force_Active_Standstill
Force the EBS to switch to Active mode, even if the vehicle is in standstill. Some of the
safety monitorings are also disable, to allow the execution of brake tests in the box
(without brake pedal activation).
This feature should only be used for the duration of the brake tests.
Leaving the EBS in active mode during maintenance work at the wheels is a major risk of
injury for the mechanics.
A prolonged active braking (longer than 2 minutes) might overheat the internal valves and
permanently damage the EBS. Bosch cannot be held responsible for any damage caused
by the mis usage of this feature.
MsgCounter_4bit and MsgChecksum_8bit_J1850
Refer to message counters and checksums section below.
EBSin_Multiswitch
Request the EBS to use the specific set of application parameters (from 0 to 5). If the sig-
nal is not available the EBS will use the default application parameters set, as configured
via RaceABS.
EBSin_ForceFaultRecovery
Request the EBS to perform a software reset, to recover from a failure state. The request is
detected when a signal goes from 0 to 1. The vehicle has to be in standstill (EB-
Sin_Chassis_vVeh_Quality == Normal(2) AND EBSin_Chassis_vVeh <= 1 m/s) . During reset,
the EBS will be silent on CAN, for up to 500 ms, and the verification of some failures can
take up to 5 seconds. The currrent state of the SW reset handling in the EBS is visible on
signal EBS_FaultRecovery_ack .

Bosch Motorsport Manual_Electronic_Brake_System_EBS 39  /  56
9.1.2 CAN Output Signal Information
EBS_CtrlMode_Ack
This signal returns the SW variant of the EBS currently in use (pressure command, torque
command, etc.)
EBS_Diag_EBS_Hardware
This bit is set to 1 if a failure has been detected on a hydraulic hardware component
(pump, valve relay, etc.)
EBS_Fcount
Returns the number of active failures currently present in the failure memory.
EBS_BPC_Mode
Indicates if the EBS is currently increasing, decreasing, or holding the pressure.
EBS_Diag_p_MC_CAN
This bit is set to 1 if a failure related to the external master cylinder pressure sensor has
been detected.
EBS_Fast_Increase_state
This bit is set to 1 if the fast increase feature is active.
EBS_BoVs_state
This bit is set to 1 if outlet switch valve is open.
EBS_BiVs_state
This bit is set to 1 if inlet switch valve is open.
EBS_BoVc2_current
This signal shows the electrical current applied to the second controllable outlet valve.
EBS_BoVc1_current
This signal shows the electrical current applied to the first controllable outlet valve.
EBS_BiVc2_current
This signal shows the electrical current applied to the second controllable inlet valve.
EBS_BiVc1_current
This signal shows the electrical current applied to the first controllable inlet valve.
EBS_CPU_Idle_Time
This signal shows the free CPU processing time.

40  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
EBS_safetyIntegrity
This signal shows the safety state of the system:
0 "full system available": no fault has been detected in the system
1 "performance related fault": at least one fault is active, but the EBS can still be used in
active state
2 "critical fault": the EBS is forced to passive state because a critical fault has been detec-
ted
3 "safety critical fault": the hydraulic braking cannot be guaranteed anymore, the vehicle
should go to the box for maintenance. This happens because a leakage on the axle side
has been detected, or because the backup separation valve is stuck.
EBS_Diag_pCaliper_extPWM
This bit is set to 1 if a failure related to the external caliper pressure sensor has been de-
tected.
EBS_Diag_pTarget_extPWM
This bit is set to 1 if a failure related to the PWM pTarget channel has been detected.
EBS_Status
This signal informs about the detailed internal status of the EBS.
0 "EBS_Status_off": The EBS is in passive mode, due to an error or an external request. The
EBS lamp will be on.
1 "EBS_Status_Diag": The EBS is currently connected with RaceABS, and is performing cal-
ibration or diagnostic routines. The EBS is generally in passive mode, but can becoming
active upon diagnostic request The EBS lamp will be on.
2 "EBS_Status_PreRun": The EBS is in passive mode, because the vehicle is in standstill. This
prevents any unnecessary activation of the valves, and avoids any potential overheating.
The EBS lamp will be off.
3 "EBS_Status_Act_WoReg_WoExt": The EBS is active, but some issues prevent the accumu-
lator to be refilled. The system will switch to passive if the accumulator is emptied. The
EBS lamp will be blinking.
4 "EBS_Status_Act_WoRegen": The EBS is active, but some safety monitorings are disabled,
because the EBS is not able to read the current electrical recuperation torque on the axle.
The EBS lamp will be blinking.
5 "EBS_Status_Act_WoBackup": The EBS is active, but some issues might prevent the EBS
to switch to passive mode. This happens when a leakage is detected, or when the backup
separation is stuck. The EBS lamp will be blinking.
6 "EBS_Status_Active": The EBS is active and fully operational. The EBS lamp will be off.
7 "EBS_Status_ActiveGoodCheck": The EBS is active and fully operational. An internal back-
ground check is ongoing, because of a failure detected during the previous power cycle.
EBS_lamp
The lamp indicates the availability of the system, based on errors and other external re-
quests. This signal should be forwarded to the dashboard to inform the driver:
0 lamp OFF: The EBS is in active mode
1 lamp ON: The EBS is in passive mode, due to an error, an ongoing diagnostic or a force
passive request

Bosch Motorsport Manual_Electronic_Brake_System_EBS 41  /  56
Blinking lamp: The EBS is in active mode but is functioning in an unsafe state. It happens
when a leakage is detected, or when some redundancy check cannot be performed due to
missing inputs.
EBS_malfunction
The lamp indicates the availability of the system, based only on errors state.
0: The EBS is in active mode
1: The EBS is in passive mode, due to an error
Toggling 0/1: The EBS is in active mode but is functioning in an unsafe state. It happens
EBS_pTarget_PWM_Quality
Quality information on PWM pTarget Channel. Refer to the extended qualifier values de-
EBS_pCaliper_PWM_Quality
Quality information on PWM pCaliper Channel. Refer to the extended qualifier values de-
EBS_pCaliper_extPwm
Caliper pressure measured by the external sensor and received via PWM.
EBS_pBrakeTarget_Ack
Target pressure request received via PWM.
EBS_pBrakeTargetGrad_Ack
Target pressure gradient as seen by the EBS after filtering.
EBS_TqM_Ctrl1_Cnt and EBS_TqM_Ctrl1_Chksum
EBS_Multiswitch_ack
Returns the index of application parameter set currently being used by the EBS. It should
equal to the requested index EBSin_Multiswitch + 1.
EBS_Diag_pAcc
This bit is set to 1 if a failure related to the pressure accumulator has been detected.
EBS_Diag_pAxle_int
This bit is set to 1 if a failure related to the EBS internal axle pressure sensor has been de-
EBS_Diag_pDriver_int
This bit is set to 1 if a failure related to the EBS internal master cylinder pressure sensor
has been detected.

42  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
EBS_PumpLocked
This bit is set to 1 if the EBS pump has been locked by diagnostic command.
EBS_pAxle_int
Axle pressure measured by the EBS internal pressure sensor.
EBS_pAxle_Quality
Quality information on the axle pressure measured by the EBS internal sensor. Refer to the
extended qualifier values description below.
EBS_pDriver_int
Master cylinder pressure measured by the EBS internal pressure sensor.
EBS_pDriver_Quality
Quality information on the master cylinder pressure measured by the EBS internal sensor.
Refer to the extended qualifier values description below.
EBS_pAccumulator
Current pressure inside the EBS accumulator. The normal operating range is between 130
and 165 bar.
EBS_pAccumulator_Quality
Quality information on the EBS accumulator pressure. Refer to the extended qualifier val-
ues description below.
EBS_RecuInfo
This signal provides braking recommendations to the VCU , based on the EBS internal
state:
0 "Recu Normal Strategy": The EBS is active, and there is no restriction on the electrical re-
cuperation.
1 "deactivate Recu, EBS in backup": The EBS is passive, and the electrical recuperation
should be deactivated, to avoid any overbraking.
2 "max Recu, no hyd. axle brake": a strong leakage has been detected between the EBS
and the calipers. No efficient hydraulic braking can be performed on this axle. Electrical
recuperation should be maximized to ensure a proper deceleration. The vehicle should re-
turn to the box for maintenance.
EBS_TqM_Info1_Cnt and EBS_TqM_Info1_Chksum
EBS_FaultRecovery_ack
This signal informs on the state of the SW Reset feature requested via the CAN signal EB-
Sin_ForceFaultRecovery . Once the reset is started ( EBS_FaultRecovery_ack == Recovery_on-
going(2) ), it cannot be interrupted. After restart, the EBS will always set the value of the
signal EBS_FaultRecovery_ack to „ Recovery_done(3) “.

Bosch Motorsport Manual_Electronic_Brake_System_EBS 43  /  56
EBS_Causal_Fault_Path
This signal contains the ID of the fault currently limiting the EBS status, if any (otherwise
0).
9.1.3 Information about Message Counters, Checksum,
and Quality Signals
Message Counters
To ensure the proper transmission of the messages, the message counter signal should be
incremented by 1 every time a new instance of this message is sent. The counter is 4 bits
long, so the values should increment from 0 to 15, and then restart a new loop from 0.
Message Checksums
To ensure the proper transmission of the messages, the message checksum should be cal-
culated every time the message is sent.
The checksum is calculated following the Autosar standard, as described in the following
document (page 22):
https://www.autosar.org/fileadmin/standards/R22-11/CP/AUTOSAR_SWS_CRCLibrary.pdf
Qualifier values description
To improve the functional safety of the system, every physical value measured by a sensor,
or an external ECU should be linked to a quality information signal. This signal informs the
receiver on the level of trust that can be given to the related physical value. The states are
defined as follow:
NoInit:
the signal source (sensor or external ECU) is not yet initialized, or the initial checks are not
complete. The associated value cannot be trusted. However, this is a temporary state,
and it should not be considered as a fault.
Normal:
the signal source (sensor or external ECU) is functioning as expected. The associated
value can be trusted.
Suspicious
the signal read from the source is out of specification, but the failure is not confirmed yet
(the debouncing time is not reached). This is a temporary state. The associated value
cannot be trusted. The receiver can consider the value as invalid or use the last valid
value.
Invalid
the signal read from the source is out of specification, and the failure is confirmed (the de-
bouncing time has been reached/exceeded). The associated value cannot be trusted.

10 | Leakage Recognition
44  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Different leakage recognition logics are present in the EBS system.
Brake Inlet Valves (from accumulator to axle)
The EBS verifies the range of activation of its brake inlet valves during initialization, and
monitors in the background that no brake fluid is flowing to the axle when the inlet valves
are closed. In case of a minor leakage, a fault will be set, but the system will remain active
if it is able to compensate this leakage. If the system does not manage to keep the actual
pressure close to the target pressure within 200 ms, the system will switch to passive and
return the control to the driver.
Brake Outlet Valves (from axle to reservoir)
The EBS verifies the range of activation of its brake outlet valves during initialization, and
monitors in the background that no brake fluid is unexpectedly flowing from the axle back
to the reservoir. In case of a minor leakage, a fault will be set, but the system will remain
active if it is able to compensate this leakage. If the system does not manage to keep the
actual pressure close to the target pressure within 200 ms, the system will switch to pass-
ive and return the control to the driver.
Backup Separation Valve
The EBS verifies the range of activation of its BSV during initialization and monitors in the
background that no brake fluid is unexpectedly flowing from or back to the master cylin-
der pipe. The active testing of the valve during normal EBS functioning are currently deac-
tivated, to avoid any unwanted influence on the pedal feeling. In case the BSV is blocked
open, the system will be passive. If the BSV is blocked closed, the system won’t be able to
switch back to passive mode. It will remain active and the different CAN signals will be set
to inform the driver of the critical safety issue.
Simulation Separation Valve (Pedal Feel Simulator)
The EBS verifies the range of activation of its SSV during initialization. The active testing of
the valve during normal EBS functioning are currently deactivated, to avoid any unwanted
influence on the pedal feeling. In case the SSV is cannot be controlled anymore, the sys-
tem will switch to passive.
Connection from EBS to reservoir
During refilling of the accumulator, the EBS monitors the pump speed and the resulting
volume flow. If the volume flow is outside of the defined range, due to air, or in case the
canal is blocked, the system will switch to passive.
Caliper Pressure Loss
Based on the calibration data, the monitoring of the pressure buildup and the pump activ-
ations, the EBS can detect an unusually high usage of brake fluid.
In such a case, the EBS will consider there is a leakage at the axle or at the calipers. The
EBS will remain in active mode and the different CAN signals will be set to inform the
driver of the critical safety issue.
This monitoring is meant to detect severe leakages at the caliper side, and Bosch recom-
mends the usage of a brake fluid level sensor to detect any fluid loss over the whole brake
circuit.

PWM Signal Description | 11
Bosch Motorsport Manual_Electronic_Brake_System_EBS 45  /  56
11 PWM Signal Description
11.1 PWM Pins
Pin 31: Sensor Ground, recommended to connect with the VCU Ground, take care of
proper GND concept, avoid Ground loops.
Pin 33: 5 V supply ( Do not connect this PIN , except when directly recommended by
Bosch).
Pin 36: PWM Channel 1 (P_Target_PWM_in).
Pin 37: PWM Channel 2 (P_Caliper_PWM_in).
11.2 PWM Hardware Interface
Signal line has EBS-internally a 3.4 kOhms pull-Up resistor (to 5 V). External PWM signal
source must either pull-down signal level actively or (preferably) supply a 5 V logic (TTL-)
signal.
Reference signal characteristics:
1 kHz PWM frequency with a signal level of 5 V for ‘high’ and 0 V for ‘low’.
Voltage Levels:
EBS Voltage Level to identify a rising edge = 2.65 V
EBS Voltage Level to identify a falling edge = 2.25 V
Usage of Bosch Motorsport ECUs:
Bosch MS 50.4: pins DIG_OUT_01…04 (pins A30-A33)
Bosch MS 7: ignition driver pins for cyl. 11 and 12 (pins A13 and A14) can be used, with
special release of generic PWM signal for these pins is set-up specifically in the IO-map.
11.3 PWM Signal Interpretation
This section of the manual has been reworked with the release of SW v06, to prevent any
misunderstanding. However, the signal interpretation is the same as before.
The EBS duty cycle is calculated as follow (duty cycle EBS = tHighLevel / tPeriod).
The EBS has a precision of 0.025 % duty cycle (4,000 Samples per period).
On both channels (Pin 36 und 37), the duty cycle operation range is 10 % - 90 %.
Duty cycles below 10 % or above 90 % are considered as invalid.
PWM Channel 1 (P_Target_PWM in; Pin 36):
Duty cycle 10 % = minimum value
Duty cycle 90 % = maximum value
The signal is interpreted differently based on EBS Variant:
-Variant 1 - signal pTarget (0 to 160 bar)
-Variant 2 - signal MTarget (0 to 16,000 Nm)
-Variant 3 – unused
PWM Channel 2 (P Caliper PWM in; Pin 37):
The duty cycle interpretation is inverted:
Duty cycle 10 % = maximum value
Duty cycle 90 % = minimum value
For all variants, the signal represents the actual brake caliper pressure (0 to 260 bar).

12 | Disposal
46  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
Hardware, accessories and packaging should be sorted for recycling in an environment-
friendly manner.
Do not dispose of this electronic device in your household waste.

Legal | 13
Bosch Motorsport Manual_Electronic_Brake_System_EBS 47  /  56
13 Legal
13.1 Legal Restrictions
Due to embargo restrictions, sale of this product in Russia, Belarus, Iran, Syria, and North
Korea is prohibited.

14 | 3D Models
48  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
You’ll find 3D Models of the EBS on our homepage www.bosch-motorsport.com

Offer Drawings | 15
Bosch Motorsport Manual_Electronic_Brake_System_EBS 49  /  56
15 Offer Drawings
15.1 Offer Drawing EBS Unit

50  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
15.2 Offer Drawing Mounting Board

Bosch Motorsport Manual_Electronic_Brake_System_EBS 51  /  56
15.3 Offer Drawing Pressure Sensor

52  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport
15.4 Wiring Diagram
PWM_IN_P/M_Target
PWM_U5V
PWM_GND
XXXX
40 A
fuse 40A
ETA
F_40A
S1
20 A
fuse 20A
F_20A
S2
25
UB_VR
AWG 12
WAU_IN1
EBS on/off
switch
SW/on_off
VCU connector
BATTERY GND
[KL31]
13
GND_MR
38
GND_ECU
XX
CAN1H
CAN1L
VCU
Vehicle Control Unit
EBS ECU connector
F02U.B00.237-01
F02U.B00.238-01
Attention :
- Bosch Motorsport recommends cables according to Raychem 55A wire spec
- Shields of CAN wires etc. to be drained to GND or VCU screen GND (if available in VCU)
- Use specified CAN wire for all CAN connections (twisted/shielded)
- No CAN resistors in the EBS ECU. CAN termination need to done according to the vehicle CAN definition.
- Malfunction lamp (MIL) sent from EBS via CAN
AWG 14 AWG 14
AWG 20
AWG 14
PWM_IN_P_Caliper
CAN1L_DC
CAN1H_DC
Wire Exit: top straight
Wire Exit: down straight
1 928 40
RL
Kabelabgang
"TOP"
Wire Exit: top 90 deg
Wire Exit: down 90 deg
L R
1 928 40 1 928 40 RL
"TOP 90"
"DOWN"
"DOWN 90"
5 A AWG 20
to choose by customer
[for example DTM06-3S]
CAN Daisy Chain
CAN-wire
X
BATTERY PLUS
[KL30]
SWITCHED PLUS
[KL15]
.F02U.S02.XXX-01 EBS Generic Wiring Diagram
F02U.S02.XXX-01
EBS Generic Wiring Diagram
BEG/MSD-NE1 HrC 20200312 SrM .
01
GaF initial drawing
AWG 22
fuse 5A
F_5A
S3
PWM Output to EBS ECU
[Target Values to be sent from
VCU to EBS ECU]
Achtung :
- Bosch Motorsport empfiehlt Kabel nach Spezifikation Raychem 55A
- Schirmungen von CAN-Leitungen mit Masse bzw. Schirm-Masse der VCU verbinden. (falls verfügbar in VCU)
- Für CAN-BUS vorgesehene Leitung für alle CAN-Verbindungen verwenden.
- Es sind keine CAN Abschlusswiderstände im EBS Steuergerät integriert. CAN Terminierung daher passend zum
weiterführenden CAN-Netzwerk im Fahrzeug auslegen.
- Fehlerstatuslampe (MIL) wird vom EBS Steuergerät via CAN zur VCU geschickt
416
AS012-35SN
DIAG MSA
Diagnosis Connector
312

Bosch Motorsport Manual_Electronic_Brake_System_EBS 53  /  56
15.5 Wiring Harness
F02U.V02.XXX-01

54  /  56 Manual_Electronic_Brake_System_EBS Bosch Motorsport

Bosch Motorsport Manual_Electronic_Brake_System_EBS 55  /  56

Bosch Engineering GmbH
Motorsport
Robert-Bosch-Allee 1
74232 Abstatt
Germany
www.bosch-motorsport.com