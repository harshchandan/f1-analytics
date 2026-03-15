{% macro calculate_championship_points(wins, podiums, points) %}
    -- Calculate a championship score combining wins, podiums, and total points
    -- Formula: (wins * 10) + (podiums * 3) + (points * 0.1)
    ({{ wins }} * 10) + ({{ podiums }} * 3) + ({{ points }} * 0.1)
{% endmacro %}