import React from 'react';
import styled from 'styled-components';
import { css } from 'styled-components';

const Container = styled.div`
    padding: 15px;
`;

const StyledButton = styled.button`
    font-size: 18px;
    font-weight: bold;
    ${props => props.red && css`
        color: #f00;
    `}
`;

const StyledButtonWithPadding = styled(StyledButton)`
    padding: 10px;
`;

const App = () => {
    return (
        <Container>
            <div>
                hello world
            </div>
            <StyledButton>
                your text here
            </StyledButton>
            <StyledButton red>
                your text here
            </StyledButton>
            <StyledButtonWithPadding>
                with padding
            </StyledButtonWithPadding>
            <StyledButtonWithPadding red>
                with padding
            </StyledButtonWithPadding>
        </Container>
    );
}

export default App;
