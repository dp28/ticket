import pytest
from unittest.mock import Mock
from unittest import TestCase

from src.commands.start_ticket import start_ticket, NotFoundError


class StartTicketTest(TestCase):

    def test_missing_ticket_throws_an_exception(self):
        mock_ticket_store = Mock()
        mock_ticket_store.get_by_id.return_value = None
        with self.assertRaises(NotFoundError):
            start_ticket('id', mock_ticket_store, Mock())

    def test_branch_is_created_with_ticket_branch_name(self):
        mock_ticket = Mock()
        mock_ticket_store = Mock()
        mock_branch_store = Mock()
        mock_ticket.get_branch_name.return_value = 'something'
        mock_ticket_store.get_by_id.return_value = mock_ticket

        start_ticket('id', mock_ticket_store, mock_branch_store)

        branch_arg = mock_branch_store.create.call_args[0][0]
        self.assertEqual('something', branch_arg.name)
