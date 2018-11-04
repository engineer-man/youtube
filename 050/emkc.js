const { challenge_id } = req.params;

const challenge = await db.challenges
    .find_one({
        where: {
            challenge_id
        }
    });

if (!challenge) return res.redirect('back');

return res.view({
    challenge
});
