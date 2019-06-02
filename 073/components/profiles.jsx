class Profiles extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            top_profiles: [
                { name: 'EM', age: 30, bio: 'is engineer man' },
                { name: 'Duckie', age: 25, bio: 'is a duck' },
                { name: 'Pizza', age: 20, bio: 'is an actual pizza' },
            ],
            other_profiles: [
                { name: 'Profile 1', age: 20, bio: 'is prof 1' },
                { name: 'Profile 2', age: 22, bio: 'is prof 2' },
                { name: 'Profile 3', age: 24, bio: 'is prof 3' },
                { name: 'Profile 4', age: 26, bio: 'is prof 4' },
                { name: 'Profile 5', age: 28, bio: 'is prof 5' },
            ]
        };
    }

    render() {
        return (
            <div>
                <h3>Top Profiles</h3>
                {this.state.top_profiles.map(profile => <Profile profile={profile} />)}

                <h3>Other Profiles</h3>
                {this.state.other_profiles.map(profile => <Profile profile={profile} />)}
            </div>
        )
    }

}
