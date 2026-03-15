{% macro calculate_championship_points(wins, podiums, points) %}
    -- Calculate a championship score combining wins, podiums, and total points
    -- Formula: (wins * 10) + (podiums * 5) + points
    ({{ wins }} * 10) + ({{ podiums }} * 5) + {{ points }}
{% endmacro %}