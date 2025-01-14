import unittest

import pusher.util


class TestUtil(unittest.TestCase):
    def test_validate_user_id(self):
        valid_user_ids = ["1", "12", "abc", "ab12", "ABCDEFG1234"]
        invalid_user_ids = ["", "x" * 201, "abc%&*"]

        for user_id in valid_user_ids:
            self.assertEqual(user_id, pusher.util.validate_user_id(user_id))

        for user_id in invalid_user_ids:
            with self.assertRaises(ValueError):
                pusher.util.validate_user_id(user_id)

    def test_validate_channel(self):
        valid_channels = ["123", "xyz", "xyz123", "xyz_123", "xyz-123", "Channel@123", "channel_xyz", "channel-xyz",
                          "channel,456", "channel;asd", "-abc_ABC@012.xpto,987;654", "#server-to-user1234",
                          "#server-to-users"]

        invalid_channels = ["#123", "x" * 201, "abc%&*"]

        for channel in valid_channels:
            self.assertEqual(channel, pusher.util.validate_channel(channel))

        for invalid_channel in invalid_channels:
            with self.assertRaises(ValueError):
                pusher.util.validate_channel(invalid_channel)

    def test_validate_server_to_user_channel(self):

        valid_server_to_user_channel = "#server-to-user-123"
        invalid_server_to_user_channel = "#server-to-useR-123"
        valid_server_to_users = "#server-to-users"
        valid_server_to_user1234 = "#server-to-user1234"

        self.assertEqual(valid_server_to_user_channel, pusher.util.validate_channel(valid_server_to_user_channel))
        self.assertEqual(valid_server_to_users, pusher.util.validate_channel(valid_server_to_users))
        self.assertEqual(valid_server_to_user1234, pusher.util.validate_channel(valid_server_to_user1234))
        with self.assertRaises(ValueError):
            pusher.util.validate_channel(invalid_server_to_user_channel)


if __name__ == '__main__':
    unittest.main()
