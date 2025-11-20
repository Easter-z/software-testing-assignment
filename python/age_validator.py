class AgeValidator:
    
    @staticmethod
    def is_valid_age(age):
        """
        验证年龄是否在有效范围内（18-65岁）
        边界值分析：17, 18, 19, 64, 65, 66
        """
        if not isinstance(age, int):
            raise TypeError("年龄必须为整数")
        
        return 18 <= age <= 65
    
    @staticmethod
    def get_age_category(age):
        """
        根据年龄分类
        等价类划分：
        - 无效类1: age < 18
        - 有效类1: 18 <= age <= 35 (青年)
        - 有效类2: 36 <= age <= 50 (中年)
        - 有效类3: 51 <= age <= 65 (中老年)
        - 无效类2: age > 65
        """
        if not AgeValidator.is_valid_age(age):
            return "无效年龄"
        
        if 18 <= age <= 35:
            return "青年"
        elif 36 <= age <= 50:
            return "中年"
        else:  # 51-65
            return "中老年"
