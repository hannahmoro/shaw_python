SELECT "ref_date", 
"cans_with_ote", 
"all_cans", 
SUM("cans_with_ote") OVER (ROWS UNBOUNDED PRECEDING) AS "cum_cans_with_ote", 
SUM("all_cans") OVER (ROWS UNBOUNDED PRECEDING) AS "cum_cans", 
SUM("cans_with_ote") OVER (ROWS UNBOUNDED PRECEDING) / SUM("all_cans") OVER (ROWS UNBOUNDED PRECEDING) * 100.0 AS "cum_percent"
FROM 
(
    SELECT "ref_date", SUM("has_any_ote_num") AS "cans_with_ote", 
    COUNT(*) AS "all_cans" *, 
    CASE WHEN ("has_any_ote" = 'Yes') THEN (1.0) WHEN NOT("has_any_ote" = 'Yes') THEN (0.0) END AS "has_any_ote_num", 
    date("referral_created_at") AS "ref_date" 
    FROM 
    (
        SELECT  *, CASE
        WHEN ("has_salary_ote" = 'No' AND "has_bonus_ote" = 'No' AND "has_equity_ote" = 'No') THEN ('No') ELSE ('Yes') END AS "has_any_ote"
        FROM 
        (
            SELECT *,
            CASE WHEN (NOT(((("amount") IS NULL)))) THEN ('Yes') WHEN ((("amount") IS NULL)) THEN ('No') END AS "has_salary_ote", 
            CASE WHEN (NOT(((("bonus") IS NULL)))) THEN ('Yes') WHEN ((("bonus") IS NULL)) THEN ('No') END AS "has_bonus_ote", 
            CASE WHEN (NOT(((("equity") IS NULL)))) THEN ('Yes') WHEN ((("equity") IS NULL)) THEN ('No') END AS "has_equity_ote"
            
            FROM (SELECT "referral_id", "LHS"."candidate_id" AS "candidate_id", "job_id", "LHS"."user_id" AS "user_id.x", "status", "position", "score", "referral_created_at", "referral_updated_at", "archived_at", "review_email_sent_at", "rationale", "last_viewed_at", "source", "archived_rationale", "archived_rationale_comment", "archived_expert_email_sent_at", "archived_expert_email_body", "archived_referral_email_sent_at", "referral_status_id", "card_status", "archive_template_index", "breakup_email_text", "automated", "screener_id", "funnel_source", "approved_at", "approval_likelihood_score", "last_email_status", "email_status_updated_at", "archived_by_id", "created_by_id", "last_updated_by_id", "deleted_at", "lead_status", "id", "RHS"."user_id" AS "user_id.y", "created_at", "updated_at", "amount", "bonus", "equity", "min_or_max", "bonus_type", "equity_type"
FROM (SELECT "id" AS "referral_id", "candidate_id", "job_id", "user_id", "status", "position", "score", "created_at" AS "referral_created_at", "updated_at" AS "referral_updated_at", "archived_at", "review_email_sent_at", "rationale", "last_viewed_at", "source", "archived_rationale", "archived_rationale_comment", "archived_expert_email_sent_at", "archived_expert_email_body", "archived_referral_email_sent_at", "referral_status_id", "card_status", "archive_template_index", "breakup_email_text", "automated", "screener_id", "funnel_source", "approved_at", "approval_likelihood_score", "last_email_status", "email_status_updated_at", "archived_by_id", "created_by_id", "last_updated_by_id", "deleted_at", "lead_status"
FROM (SELECT "id", "candidate_id", "job_id", "user_id", "status", "position", "score", "created_at", "updated_at", "archived_at", "review_email_sent_at", "rationale", "last_viewed_at", "source", "archived_rationale", "archived_rationale_comment", "archived_expert_email_sent_at", "archived_expert_email_body", "archived_referral_email_sent_at", "referral_status_id", "card_status", "archive_template_index", "breakup_email_text", "automated", "screener_id", "funnel_source", "approved_at", "approval_likelihood_score", "last_email_status", "email_status_updated_at", "archived_by_id", "created_by_id", "last_updated_by_id", "deleted_at", "lead_status"
FROM (SELECT "id", "candidate_id", "job_id", "user_id", "status", "position", "score", "created_at", "updated_at", "archived_at", "review_email_sent_at", "rationale", "last_viewed_at", "source", "archived_rationale", "archived_rationale_comment", "archived_expert_email_sent_at", "archived_expert_email_body", "archived_referral_email_sent_at", "referral_status_id", "card_status", "archive_template_index", "breakup_email_text", "automated", "screener_id", "funnel_source", "approved_at", "approval_likelihood_score", "last_email_status", "email_status_updated_at", "archived_by_id", "created_by_id", "last_updated_by_id", "deleted_at", "lead_status", RANK() OVER (PARTITION BY "candidate_id" ORDER BY "created_at" DESC) AS "q01"
FROM "referrals") "q01"
WHERE ("q01" <= 1)) "q02") "LHS"
LEFT JOIN (SELECT "id", "user_id", "candidate_id", "created_at", "updated_at", "amount", "bonus", "equity", "min_or_max", "bonus_type", "equity_type"
FROM (SELECT "id", "user_id", "candidate_id", "created_at", "updated_at", "amount", "bonus", "equity", "min_or_max", "bonus_type", "equity_type", RANK() OVER (PARTITION BY "candidate_id" ORDER BY "updated_at" DESC) AS "q01"
FROM "compensations") "q01"
WHERE ("q01" <= 1)) "RHS"
ON ("LHS"."candidate_id" = "RHS"."candidate_id")
) "q02") "q03") "q04") "q05"
WHERE ("referral_created_at" > '2022-03-31')
GROUP BY "ref_date") "q06"