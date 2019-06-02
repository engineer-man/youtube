class Profile extends React.Component {

    render() {
        return (
            <div>
                <img src="https://uploads.mixer.com/avatar/jf7qalfa-8499245.jpg" />
                <Name name={this.props.profile.name} />
                <p>
                    age: {this.props.profile.age}
                    <br />
                    bio: {this.props.profile.bio}
                </p>
            </div>
        )
    }

}
