#include "main.h"

//###################################################################
#define VL6180X_PRESS_HUM_TEMP	0
#define MPU9250	1
#define DYN_ANEMO 0
//###################################################################

//====================================================================
//			CAN ACCEPTANCE FILTER
//====================================================================
#define USE_FILTER	1
// Can accept until 4 Standard IDs
#define ID_1	0x01
#define ID_2	0x02
#define ID_3	0x03
#define ID_4	0x04
//====================================================================
#define PI 3.14
    int16_t accel_data[3];
    float accel_xyz[3];
    int16_t gyro_data[3];
    float gyro_xyz[3];

    float R12;
    float R22;
    float R31;
    float R32;
    float R33;

    int phi;
    int theta;
    int psi;



extern void systemClock_Config(void);

void (*rxCompleteCallback) (void);
void can_callback(void);

CAN_Message      rxMsg;
CAN_Message      txMsg;
long int        counter = 0;

uint8_t* aTxBuffer[2];

extern float magCalibration[3];

void VL6180x_Init(void);
void VL6180x_Step(void);

int status;
int new_switch_state;
int switch_state = -1;
int send_data = 0;

//====================================================================
// >>>>>>>>>>>>>>>>>>>>>>>>>> MAIN <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
//====================================================================
int main(void)
{
	HAL_Init();
	systemClock_Config();
    SysTick_Config(HAL_RCC_GetHCLKFreq() / 1000); //SysTick end of count event each 1ms
	uart2_Init();
	uart1_Init();
	i2c1_Init();

#if DYN_ANEMO
    anemo_Timer1Init();
#endif

	HAL_Delay(1000); // Wait

#if VL6180X_PRESS_HUM_TEMP
    VL6180x_Init();
#endif

#if MPU9250
    mpu9250_InitMPU9250();
    mpu9250_CalibrateMPU9250();
#if USE_MAGNETOMETER
    mpu9250_InitAK8963(magCalibration);
#endif
    uint8_t response=0;
	response =  mpu9250_WhoAmI();
	term_printf("%d",response);
#endif


    can_Init();
    can_SetFreq(CAN_BAUDRATE); // CAN BAUDRATE : 500 MHz -- cf Inc/config.h
#if USE_FILTER
    //can_Filter_list((ID_1<<21)|(ID_2<<5) , (ID_3<<21)|(ID_4<<5) , CANStandard, 0); // Accept until 4 Standard IDs
    uint32_t id1_id2 = (ID_3 << 5);  // ID 1 dans le champ 16 bits
    uint32_t id3_id4 = 0x00000000;   // Pas d'autres ID

    can_Filter_list(id1_id2, id3_id4, CANStandard, 0);
#else
    can_Filter_disable(); // Accept everybody
#endif
    can_IrqInit();
    can_IrqSet(&can_callback);

    txMsg.id=0x55;
    txMsg.data[0]=1;
    txMsg.data[1]=2;
    txMsg.len=2;
    txMsg.format=CANStandard;
    txMsg.type=CANData;

    can_Write(txMsg);

    // Décommenter pour utiliser ce Timer ; permet de déclencher une interruption toutes les N ms
    // tickTimer_Init(200); // period in ms

#if DYN_ANEMO
   // TEST MOTEUR
    dxl_LED(1, LED_ON);
    HAL_Delay(500);
    dxl_LED(1, LED_OFF);
    HAL_Delay(500);

    dxl_torque(1, TORQUE_OFF);
    dxl_setOperatingMode(1, VELOCITY_MODE);
    dxl_torque(1, TORQUE_ON);
    dxl_setGoalVelocity(1, 140);
    HAL_Delay(5000);
    dxl_setGoalVelocity(1, 0);
#endif


    while (1) {


#if DYN_ANEMO

#endif

#if VL6180X_PRESS_HUM_TEMP
    VL6180x_Step();


#endif



#if MPU9250
    mpu9250_ReadAccelData(accel_data);
       mpu9250_ReadGyroData(gyro_data);
       for(int i=0; i<3; i++)
           	    {
           	    	accel_xyz[i] = accel_data[i]*4.0/32768.0;
           	    	gyro_xyz[i] = gyro_data[i]*(1000.0/32768.0)*(PI/180.0);
           	    }
           	    MadgwickAHRSupdateIMU(gyro_xyz[0], gyro_xyz[1], gyro_xyz[2], accel_xyz[0], accel_xyz[1], accel_xyz[2]);
           	    R12 = 2 * (q1*q2 + q0 * q3);
           	    R22 = q0*q0 + q1*q1 - q2*q2 - q3*q3;
           		R31 = 2*(q0*q1 + q2*q3);
           		R32 = 2*(q1*q3 - q0*q2);
           		R33 = q0*q0 - q1*q1 - q2*q2 + q3*q3;
           		phi = (int)(atan2(R31,R33)*(180/3.1415) + 180);
           		theta = (int)(-asin(R32)*(180/3.1415) + 180);
           		psi = (int)(atan2(R12,R22)*(180/3.1415) + 180);
           		term_printf("position: PHI: %d , THETA: %d, PSI: %d\n\r",phi, theta, psi);
           		if (send_data)
           		{
					txMsg.id=0x57;
						txMsg.data[0]=(phi>>8);
						txMsg.data[1]=(phi>>0);
						txMsg.data[2]=(theta>>8);
						txMsg.data[3]=(theta>>0);
						txMsg.data[4]=(psi>>8);
						txMsg.data[5]=(psi>>0);
						txMsg.len=6;
						txMsg.format=CANStandard;
						txMsg.type=CANData;

						can_Write(txMsg);
						send_data = 0;
           		}
#endif

    }
	return 0;
}


//====================================================================
//			CAN CALLBACK RECEPT
//====================================================================

void can_callback(void)
{
	CAN_Message msg_rcv;

	can_Read(&msg_rcv);
	if (msg_rcv.data[0] == 1)
	{
		send_data = 1;
	}
}
//====================================================================
//			TIMER CALLBACK PERIOD
//====================================================================

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
	//term_printf("from timer interrupt\n\r");
}
//====================================================================

#if VL6180X_PRESS_HUM_TEMP
void VL6180x_Init(void)
{
	uint8_t id;
	State.mode = 1;

    XNUCLEO6180XA1_Init();
    HAL_Delay(500); // Wait
    // RESET
    XNUCLEO6180XA1_Reset(0);
    HAL_Delay(10);
    XNUCLEO6180XA1_Reset(1);
    HAL_Delay(1);

    HAL_Delay(10);
    VL6180x_WaitDeviceBooted(theVL6180xDev);
    id=VL6180x_Identification(theVL6180xDev);
    term_printf("id=%d, should be 180 (0xB4) \n\r", id);
    VL6180x_InitData(theVL6180xDev);

    State.InitScale=VL6180x_UpscaleGetScaling(theVL6180xDev);
    State.FilterEn=VL6180x_FilterGetState(theVL6180xDev);

     // Enable Dmax calculation only if value is displayed (to save computation power)
    VL6180x_DMaxSetState(theVL6180xDev, DMaxDispTime>0);

    switch_state=-1 ; // force what read from switch to set new working mode
    State.mode = AlrmStart;
}
//====================================================================
void VL6180x_Step(void)
{
    DISP_ExecLoopBody();

    new_switch_state = XNUCLEO6180XA1_GetSwitch();
    if (new_switch_state != switch_state) {
        switch_state=new_switch_state;
        status = VL6180x_Prepare(theVL6180xDev);
        // Increase convergence time to the max (this is because proximity config of API is used)
        VL6180x_RangeSetMaxConvergenceTime(theVL6180xDev, 63);
        if (status) {
            AbortErr("ErIn");
        }
        else{
            if (switch_state == SWITCH_VAL_RANGING) {
                VL6180x_SetupGPIO1(theVL6180xDev, GPIOx_SELECT_GPIO_INTERRUPT_OUTPUT, INTR_POL_HIGH);
                VL6180x_ClearAllInterrupt(theVL6180xDev);
                State.ScaleSwapCnt=0;
                DoScalingSwap( State.InitScale);
            } else {
                 State.mode = RunAlsPoll;
                 InitAlsMode();
            }
        }
    }

    switch (State.mode) {
    case RunRangePoll:
        RangeState();
        break;

    case RunAlsPoll:
        AlsState();
        break;

    case InitErr:
        TimeStarted = g_TickCnt;
        State.mode = WaitForReset;
        break;

    case AlrmStart:
       GoToAlaramState();
       break;

    case AlrmRun:
        AlarmState();
        break;

    case FromSwitch:
        // force reading swicth as re-init selected mode
        switch_state=!XNUCLEO6180XA1_GetSwitch();
        break;

    case ScaleSwap:

        if (g_TickCnt - TimeStarted >= ScaleDispTime) {
            State.mode = RunRangePoll;
            TimeStarted=g_TickCnt; /* reset as used for --- to er display */
        }
        else
        {
        	DISP_ExecLoopBody();
        }
        break;

    default: {
    	 DISP_ExecLoopBody();
          if (g_TickCnt - TimeStarted >= 5000) {
              NVIC_SystemReset();
          }
    }
    }
}
#endif
//====================================================================

