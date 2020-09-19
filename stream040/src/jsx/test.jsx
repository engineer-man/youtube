import React from 'react';
import ReactDOM from 'react-dom';

class Test extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            add_item_text: '',
            todo: [
                {
                    name: 'pet chase',
                    done: true
                },
                {
                    name: 'clean chase',
                    done: false
                }
            ]
        };

        this.update_done = this.update_done.bind(this);
        this.item_text = this.item_text.bind(this);
        this.add = this.add.bind(this);
    }

    update_done(id) {
        this.setState({
            todo: this.state.todo.map((item, i) => {
                if (i === id) {
                    item.done = !item.done;
                }

                return item;
            })
        })
    }

    item_text(e) {
        this.setState({
            add_item_text: e.target.value
        });
    }

    add() {
        this.setState({
            add_item_text: '',
            todo: [
                ...this.state.todo,
                {
                    name: this.state.add_item_text,
                    done: false
                }
            ]
        })
    }

    render() {
        return (
            <div>
                <h4>Todo</h4>
                {this.state.todo.map((item, i) => {
                    return (
                        <div key={i}>
                            <input
                                type="checkbox"
                                checked={item.done}
                                onChange={() => this.update_done(i)} />
                            {item.name}
                            {', '}
                            done? = {item.done ? 'yes' : 'no'}
                        </div>
                    );
                })}
                <input
                    type="text"
                    id="add"
                    onChange={this.item_text}
                    value={this.state.add_item_text} />
                <button
                    type="button"
                    onClick={this.add}>add</button>
            </div>
        );
    }
}

ReactDOM.render(
    React.createElement(Test, {}),
    document.getElementById('test')
);

export default Test;
