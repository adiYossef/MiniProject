class GeneralNeuron:
    def __init__(self, firing_rate):
        self.firing_rate = firing_rate

    def Activate(self):
        pass


class MotorNeuron(GeneralNeuron):
    def __init__(self, firing_rate, taget_muscle):
        super().__init__(firing_rate)
        self.taget_muscle = taget_muscle
        
    def ControlMuscle(self, activation_level):
        pass

class SensoryNeuron(GeneralNeuron):
    def __init__(self, firing_rate, receptor_type):
        super().__init__(firing_rate)
        self.receptor_type = receptor_type
    
    def SenseStimulus(self, stimulus):
        pass


class Photoreceptor(SensoryNeuron):
    def __init__(self, firing_rate):
        super().__init__(firing_rate, "light")
    
    def LightDetection(self, light_intensity):
        self.SenseStimulus(stimulus=light_intensity)

class Mechanoreceptor(SensoryNeuron):
    def __init__(self, firing_rate):
        super().__init__(firing_rate, "pressure")
    
    def PressureDetection(self, pressure):
        self.SenseStimulus(stimulus=pressure)


class AlphaMotorNeuron(MotorNeuron):
    def __init__(self, firing_rate):
        super().__init__(firing_rate, "skeletal muscle")
    
    def SkeletalMuscleControl(self):
        self.ControlMuscle(self.Activate())


class GammaMotorNeuron(MotorNeuron):
    def __init__(self, firing_rate,):
        super().__init__(firing_rate, "muscle spindle")
    
    def MuscleSpindleControl(self):
        self.ControlMuscle(self.Activate())



