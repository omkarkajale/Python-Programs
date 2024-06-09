def are_anagrams(str1, str2):
    # Helper function to clean and sort a string
    def clean_string(s):
        return sorted(''.join(filter(str.isalpha, s.lower())))

    return clean_string(str1) == clean_string(str2)

# Test cases
print(are_anagrams("listen", "silent"))  # Should return True
print(are_anagrams("hello", "billion"))  # Should return False
print(are_anagrams("Dormitory", "Dirty room"))  # Should return True
print(are_anagrams("The eyes", "They see"))  # Should return True
print(are_anagrams("Astronomer", "Moon starer"))  # Should return True
