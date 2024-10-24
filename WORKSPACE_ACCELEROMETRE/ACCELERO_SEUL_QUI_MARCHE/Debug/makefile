################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include startup/subdir.mk
-include src/vl6180x/subdir.mk
-include src/subdir.mk
-include Utilities/STM32F1xx_Nucleo/subdir.mk
-include HAL_Driver/Src/subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

OPTIONAL_TOOL_DEPS := \
$(wildcard ../makefile.defs) \
$(wildcard ../makefile.init) \
$(wildcard ../makefile.targets) \


BUILD_ARTIFACT_NAME := ACCELERO_SEUL_QUI_MARCHE
BUILD_ARTIFACT_EXTENSION := elf
BUILD_ARTIFACT_PREFIX :=
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME)$(if $(BUILD_ARTIFACT_EXTENSION),.$(BUILD_ARTIFACT_EXTENSION),)

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
ACCELERO_SEUL_QUI_MARCHE.elf \

MAP_FILES += \
ACCELERO_SEUL_QUI_MARCHE.map \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
ACCELERO_SEUL_QUI_MARCHE.list \

OBJCOPY_BIN += \
ACCELERO_SEUL_QUI_MARCHE.bin \


# All Target
all: main-build

# Main-build Target
main-build: ACCELERO_SEUL_QUI_MARCHE.elf secondary-outputs

# Tool invocations
ACCELERO_SEUL_QUI_MARCHE.elf ACCELERO_SEUL_QUI_MARCHE.map: $(OBJS) $(USER_OBJS) /home/e2024/e24tello/Documents/Projet-BUS-CAN/WORKSPACE/ACCELERO_SEUL_QUI_MARCHE/LinkerScript.ld makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-gcc -o "ACCELERO_SEUL_QUI_MARCHE.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m3 -T"/home/e2024/e24tello/Documents/Projet-BUS-CAN/WORKSPACE/ACCELERO_SEUL_QUI_MARCHE/LinkerScript.ld" --specs=nosys.specs -Wl,-Map="ACCELERO_SEUL_QUI_MARCHE.map" -Wl,--gc-sections -static --specs=nano.specs -mfloat-abi=soft -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

ACCELERO_SEUL_QUI_MARCHE.list: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "ACCELERO_SEUL_QUI_MARCHE.list"
	@echo 'Finished building: $@'
	@echo ' '

ACCELERO_SEUL_QUI_MARCHE.bin: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "ACCELERO_SEUL_QUI_MARCHE.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) ACCELERO_SEUL_QUI_MARCHE.bin ACCELERO_SEUL_QUI_MARCHE.elf ACCELERO_SEUL_QUI_MARCHE.list ACCELERO_SEUL_QUI_MARCHE.map default.size.stdout
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

fail-specified-linker-script-missing:
	@echo 'Error: Cannot find the specified linker script. Check the linker settings in the build configuration.'
	@exit 2

warn-no-linker-script-specified:
	@echo 'Warning: No linker script specified. Check the linker settings in the build configuration.'

.PHONY: all clean dependents main-build fail-specified-linker-script-missing warn-no-linker-script-specified

-include ../makefile.targets
