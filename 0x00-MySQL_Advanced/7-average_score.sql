-- Create a stored procedure ComputeAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    SELECT SUM(score), COUNT(DISTINCT project_id)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update the average score for the user
    UPDATE users
    SET average_score = (total_score / total_projects)
    WHERE id = p_user_id;
END;
//
DELIMITER ;
