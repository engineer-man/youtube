const { challenge_id } = req.params;

return db.challenges
    .find_one({
        where: {
            challenge_id
        }
    })
    .then(challenge => {
        if (!challenge) return res.redirect('back');

        return res.view({
            challenge
        });
    });
