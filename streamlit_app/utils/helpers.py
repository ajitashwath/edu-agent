def validate_inputs(academic_percentage, school_name, age):
    errors = []
    if not (40.0 <= academic_percentage <= 100.0):
        errors.append("Academic percentage must be between 40 and 100.")
    if not school_name or not school_name.strip():
        errors.append("School name cannot be empty.")
    if not (14 <= age <= 22):
        errors.append("Age must be between 14 and 22.")
    return errors


def calculate_preparation_time(age, current_class):
    """
    Estimate months left for JEE preparation based on age and class.
    """
    # Example logic: younger students have more time
    if current_class == "10th Grade":
        return 24 - (age - 15) * 12  # up to 2 years
    elif current_class == "11th Grade":
        return 18 - (age - 16) * 12  # up to 1.5 years
    elif current_class == "12th Grade":
        return 12 - (age - 17) * 12  # up to 1 year
    elif "Passed" in current_class:
        return 6  # gap year, 6 months assumed
    else:
        return 12  # default 1 year
